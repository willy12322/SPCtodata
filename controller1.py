from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from matplotlib.patches import Circle, PathPatch
from test5 import Ui_MainWindow
import mpl_toolkits.mplot3d.art3d as art3d
from itertools import product
from mpl_toolkits.mplot3d import proj3d
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
import time



def text3d(ax, xyz, s, zdir="z", size=None, angle=0, usetex=False, **kwargs):
    """
    Plots the string *s* on the axes *ax*, with position *xyz*, size *size*,
    and rotation angle *angle*. *zdir* gives the axis which is to be treated as
    the third dimension. *usetex* is a boolean indicating whether the string
    should be run through a LaTeX subprocess or not.  Any additional keyword
    arguments are forwarded to `.transform_path`.

    Note: zdir affects the interpretation of xyz.
    """
    x, y, z = xyz
    if zdir == "y":
        xy1, z1 = (x, z), y
    elif zdir == "x":
        xy1, z1 = (y, z), x
    else:
        xy1, z1 = (x, y), z

    text_path = TextPath((0, 0), s, size=size, usetex=usetex)
    trans = Affine2D().rotate(angle).translate(xy1[0], xy1[1])

    p1 = PathPatch(trans.transform_path(text_path), **kwargs)
    ax.add_patch(p1)
    art3d.pathpatch_2d_to_3d(p1, z=z1, zdir=zdir)

def pathpatch_2d_to_3d(pathpatch, z = 0, normal = 'z'):
    """
    Transforms a 2D Patch to a 3D patch using the given normal vector.

    The patch is projected into they XY plane, rotated about the origin
    and finally translated by z.
    """

def rotation_matrix(d):
    """
    Calculates a rotation matrix given a vector d. The direction of d
    corresponds to the rotation axis. The length of d corresponds to
    the sin of the angle of rotation.

    Variant of: http://mail.scipy.org/pipermail/numpy-discussion/2009-March/040806.html
    """
    sin_angle = np.linalg.norm(d)

    if sin_angle == 0:
        return np.identity(3)

    d /= sin_angle

    eye = np.eye(3)
    ddt = np.outer(d, d)
    skew = np.array([[    0,  d[2],  -d[1]],
                  [-d[2],     0,  d[0]],
                  [d[1], -d[0],    0]], dtype=np.float64)

    M = ddt + np.sqrt(1 - sin_angle**2) * (eye - ddt) + sin_angle * skew
    return M

def pathpatch_2d_to_3d(pathpatch, z = 0, normal = 'z'):
    """
    Transforms a 2D Patch to a 3D patch using the given normal vector.

    The patch is projected into they XY plane, rotated about the origin
    and finally translated by z.
    """
    if type(normal) is str: #Translate strings to normal vectors
        index = "xyz".index(normal)
        normal = np.roll((1.0,0,0), index)

    normal /= np.linalg.norm(normal) #Make sure the vector is normalised

    path = pathpatch.get_path() #Get the path and the associated transform
    trans = pathpatch.get_patch_transform()

    path = trans.transform_path(path) #Apply the transform

    pathpatch.__class__ = art3d.PathPatch3D #Change the class
    pathpatch._code3d = path.codes #Copy the codes
    pathpatch._facecolor3d = pathpatch.get_facecolor #Get the face color

    verts = path.vertices #Get the vertices in 2D

    d = np.cross(normal, (0, 0, 1)) #Obtain the rotation vector
    M = rotation_matrix(d) #Get the rotation matrix

    pathpatch._segment3d = np.array([np.dot(M, (x, y, 0)) + (0, 0, z) for x, y in verts])

def pathpatch_translate(pathpatch, delta):
    """
    Translates the 3D pathpatch by the amount delta.
    """
    pathpatch._segment3d += delta

class MainWindow_controller(QtWidgets.QMainWindow):
    readDialIndicator = pyqtSignal(str,str,str)
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.DialIndicator_init()
        self.ReferenceTiltAngle_init()
        self.readDialIndicator.connect(self.setup_control)
        #self.ui.pushButton.clicked.connect(self.send_signal)

    def send_signal(self,value12,value04,value08):

        self.readDialIndicator.emit(value12, value04, value08)

    def setup_control(self,value12,value04,value08):

        self.ui.value_12.setText(value12)
        self.ui.value_04.setText(value04)
        self.ui.value_08.setText(value08)

        value12 = str(value12).split(" ")[0]
        value04 = str(value04).split(" ")[0]
        value08 = str(value08).split(" ")[0]

        average = (float(value12) + float(value04) + float(value08))/3
        y = float(value12)
        x_04 = float(value04)
        x_08 = float(value08)

        if y < average:
            y_current_state = "12點方向較高"
            normal_y = (0,-1,1)
        elif y > average:
            y_current_state = "06點方向較高"
            normal_y = (0, 1, 1)
        else:
            y_current_state = "不用調整"
            normal_y = (0, 0, 1)

        if  x_04 < x_08:
            x_current_state = "03點方向較高"
            normal_x = (-1, 0, 1)
        elif x_04 > x_08:
            x_current_state = "09點方向較高"
            normal_x = (1, 0, 1)
        else:
            x_current_state = "x軸不用調整"
            normal_x = (0, 0, 1)

        self.ui.label_11.setText(y_current_state)
        self.ui.x_value.setText(x_current_state)

        self.canvas_1 = FigureCanvas(self.drew_3d_y((normal_y)))
        self.graphicscene_1 = QtWidgets.QGraphicsScene()
        self.graphicscene_1.setSceneRect(0, 0, 300, 280)
        self.graphicscene_1.addWidget(self.canvas_1)
        self.ui.ReferenceTiltAngle_y.setScene(self.graphicscene_1)

        self.canvas_2 = FigureCanvas(self.drew_3d_x((normal_x)))
        self.graphicscene_2 = QtWidgets.QGraphicsScene()
        self.graphicscene_2.setSceneRect(0, 0, 300, 280)
        self.graphicscene_2.addWidget(self.canvas_2)
        self.ui.ReferenceTiltAngle_x.setScene(self.graphicscene_2)

    def DialIndicator_init(self):

        self.canvas = FigureCanvas(self.drew_init())
        self.graphicscene = QtWidgets.QGraphicsScene()
        self.graphicscene.setSceneRect(0, 0, 700, 600)
        self.graphicscene.addWidget(self.canvas)
        self.ui.DialIndicator.setScene(self.graphicscene)

    def drew_init(self, i=0):
        fig = plt.figure(figsize=(7,6), dpi=100)
        ax = plt.axes(xlim=(-1, 5), ylim=(-1, 5))

        circle_1, = ax.plot([], [],color='red')
        circle_1.set_data([], [])
        radius = 2
        x = np.ogrid[0:4:0.0001]
        y = np.sqrt(4 - (x - 2) ** 2) + 2
        circle_1.set_data(x, y)

        circle_2, = ax.plot([], [],color='red')
        x = np.ogrid[0:4:0.0001]
        y = -np.sqrt(4 - (x - 2) ** 2) + 2
        circle_2.set_data(x, y)

        x = [2, 2, 2, 2,2]
        y = [2, 2.5, 3, 3.5,4]
        plt.plot(x, y, color='yellow')

        x = np.ogrid[0.6:2:0.01]
        y = x

        plt.plot(x, y, color='yellow')

        x = np.ogrid[2:3.4:0.01]
        y = -x +4

        plt.plot(x, y, color='yellow')

        plt.close()
        return fig

    def ReferenceTiltAngle_init(self):

        self.canvas_1 = FigureCanvas(self.drew_3d_y((0,1,1)))
        self.graphicscene_1 = QtWidgets.QGraphicsScene()
        self.graphicscene_1.setSceneRect(0, 0, 300, 280)
        self.graphicscene_1.addWidget(self.canvas_1)
        self.ui.ReferenceTiltAngle_y.setScene(self.graphicscene_1)

        self.canvas_2 = FigureCanvas(self.drew_3d_x((1,0,1)))
        self.graphicscene_2= QtWidgets.QGraphicsScene()
        self.graphicscene_2.setSceneRect(0, 0, 300, 280)
        self.graphicscene_2.addWidget(self.canvas_2)
        self.ui.ReferenceTiltAngle_x.setScene(self.graphicscene_2)

    def drew_3d_y(self, normal_y):
        fig = plt.figure(figsize=(3.5,2.5), dpi=100)
        ax = fig.add_subplot(projection='3d')

        p = Circle((0, 0), .5, facecolor='r',alpha=0.3)
        ax.add_patch(p)
        pathpatch_2d_to_3d(p, z=0,normal = normal_y)
        pathpatch_translate(p, 0.5)

        p = Circle((0, 0), .5, facecolor='b',alpha=0.8)
        ax.add_patch(p)
        pathpatch_2d_to_3d(p, z=0)
        pathpatch_translate(p, 0.5)

        ax.view_init(5, 0)

        plt.close()
        return fig

    def drew_3d_x(self, normal_x):
        fig = plt.figure(figsize=(3.5,2.5), dpi=100)
        ax = fig.add_subplot(projection='3d')

        p = Circle((0, 0), .5, facecolor='r',alpha=0.3)
        ax.add_patch(p)
        pathpatch_2d_to_3d(p, z=0,normal = normal_x)
        pathpatch_translate(p, 0.5)

        p = Circle((0, 0), .5, facecolor='b',alpha=0.8)
        ax.add_patch(p)
        pathpatch_2d_to_3d(p, z=0)
        pathpatch_translate(p, 0.5)

        ax.view_init(5, -90)

        plt.close()
        return fig
