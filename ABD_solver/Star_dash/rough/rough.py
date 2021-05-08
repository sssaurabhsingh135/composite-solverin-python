import numpy as np
import numpy.linalg as lg
from CLPTC.calculator.input_file_reader import ply_properties,mat_properties

class Lamina():
    '''
    Note:
         Positive axis - the same direction as the direction of the ply fiber is the positive axis, expressed in 1, 2, 3 directions
         Off-axis - generally the coordinate system defined by the natural axis of the laminate, expressed in x, y, z, relative to the coordinate system of the ply
         Laying angle - the angle between the off-axis x and the positive axis 1, and the counterclockwise rotation is positive
         Poisson's ratio - Poisson's ratio is defined by foreign books and software, namely ν_12=-ε_2/ε_1, ν_21=-ε_1/ε_2
                             Use nu12, nu12 (OptiStruct) = nuxy (ANSYS) = ν_12 (foreign textbooks) = ν_1 (composite material mechanics) = ν_21 (composite material mechanics) = -ε_2/ε_1

    matid      material id
    e1         Young Modulus in direction 1
    e2         Young Modulus in direction 2
    g12        in-plane shear modulus

    nu21       Poisson's ratio 21,nu21=-ε2/ε1
    nu12       Poisson's ratio 12: use formula nu21/e1 = nu12/e2


    st1,st2    allowable tensile stresses for directions 1 and 2
    sc1,sc2    allowable compressive stresses for directions 1 and 2
    ss12       allowable in-plane stress for shear
    strn       allowable strain for direction 1


    plyid      id of the composite lamina
    t           ply thickness
    theta       ply angle

         S (single layer) positive axis compliance matrix
         Q (single-layer) positive-axis modulus matrix

         T_stress stress conversion matrix
         T_strain strain transformation matrix

         S_offaxis (single layer) off-axis compliance matrix
         Q_offaxis (single layer) off-axis modulus matrix

         Sij compliance component
         Qij modulus component

    '''
    def __init__(self):
        self.matid    = None
        self.plyid    = None
        self.t        = None
        self.theta    = None


        self.e1   = None
        self.e2   = None
        self.g12  = None
        self.nu21 = None
        self.nu12 = None
        self.st1  = None
        self.st2  = None
        self.sc1  = None
        self.sc2  = None
        self.ss12 = None
        self.strn = None



        self.S        = None
        self.Q        = None
        self.T_stress = None
        self.T_strain = None
        self.S_offaxis= None
        self.Q_offaxis= None

        self.lamina_Ex  = None
        self.lamina_Ey  = None
        self.lamina_Gxy = None
        self.lamina_nuxy= None



        self.laminates= []
        self.cos      = None
        self.cos2t    = None
        self.sin      = None
        self.sin2t    = None

    def calc_SQ(self):

        '''
                 Calculate the positive axis stiffness of a single layer
                 :return: Only return S and Q, the variables such as s11 in the middle cannot be accessed
        '''
        e1 = self.e1
        e2 = self.e2
        nu21 = self.nu21
        nu12 = self.nu12
        g12 = self.g12

        s11 = 1 / e1
        s22 = 1 / e2
        s66 = 1 / g12
        s12 = -nu12 / e2
        s21 = -nu21 / e1
        s16 = s61 = s26 = s62 = 0

        qm  = (1 - nu21*nu12)
        q11 = e1/qm
        q22 = e2/qm
        q66 = g12
        q12 = nu12 * e1/qm
        q21 = nu21 * e2/qm
        q16 = q61 = q26 = q62 = 0

        self.S = np.array(
            [[s11,s12,s16],
             [s21,s22,s26],
             [s61,s62,s66]],dtype = float)

        self.Q = np.array(
            [[q11,q12,q16],
             [q21,q22,q26],
             [q61,q62,q66]],dtype = float)

        # Calculate the off-axis stiffness of each single layer
        theta = self.theta

        self.cos   = np.cos( np.deg2rad(   theta ) )
        self.sin   = np.sin( np.deg2rad(   theta ) )
        # self.cos2t = np.cos( np.deg2rad( 2*self.theta ) )
        # self.sin2t = np.sin( np.deg2rad( 2*self.theta ) )
        cos    = self.cos
        sin    = self.sin
        cos2   = cos**2
        sin2   = sin**2
        sincos = sin*cos
        # cos2t  = self.cos2t
        # sin2t  = self.sin2t

        # Stress conversion matrix, used to convert off-axis stress to normal axial stress
        self.T_stress = np.array(
            [[   cos2,  sin2,  2*sincos],
             [   sin2,  cos2, -2*sincos],
             [-sincos,sincos, cos2-sin2]],dtype=float)

        # Strain conversion matrix, used to convert off-axis strain to normal-axis strain
        self.T_strain = np.array(
            [[     cos2,    sin2,    sincos],
             [     sin2,    cos2,   -sincos],
             [-2*sincos,2*sincos, cos2-sin2]],dtype=float)

        # Calculate the off-axis stiffness matrix
        self.Q_offaxis = np.dot(np.dot(lg.inv(self.T_stress), self.Q), self.T_strain)
        self.S_offaxis = np.dot(np.dot(lg.inv(self.T_strain), self.S), self.T_stress)

        # Laying equivalent engineering elastic constant
        self.lamina_Ex  = 1/self.S_offaxis[0,0]
        self.lamina_Ey  = 1/self.S_offaxis[1,1]
        self.lamina_Gxy = 1/self.S_offaxis[2,2]
        self.lamina_nuxy= -self.lamina_Ex*self.S_offaxis[0,1]

def Get_lamina_prop(plyid):
    lamina_prop = Lamina()

    #Laying attributes
    lamina_prop.matid = ply_properties['Material index value'][plyid]
    lamina_prop.t     = ply_properties['thickness'][plyid]
    lamina_prop.theta = ply_properties['Laying angle'][plyid]

    # Material properties of the layer
    lamina_prop.e1   = mat_properties['E1'][lamina_prop.matid]
    lamina_prop.e2   = mat_properties['E2'][lamina_prop.matid]
    lamina_prop.nu21 = mat_properties['nu21'][lamina_prop.matid]
    lamina_prop.g12  = mat_properties['G12'][lamina_prop.matid]
    lamina_prop.nu12 = lamina_prop.nu21/lamina_prop.e1*lamina_prop.e2

    lamina_prop.calc_SQ()


    return lamina_prop