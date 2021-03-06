#!/usr/bin/env python

from __future__ import print_function
from slamdog_srv_navi.srv import *
import rospy
import os


def get_loc(req):
    print("Returning %s" % (req.a + " from client"))
    os.system("rosrun slamdog_navi slamdog_navi _id:=" + req.a)
    return dataLoaderResponse(req.a + " from client")


def send_data_loc_server():
    rospy.init_node('send_loc_data', anonymous=False)
    s = rospy.Service('send_loc_data', dataLoader, get_loc)
    print("Ready to get Location from Client.")
    rospy.spin()


if __name__ == "__main__":
    send_data_loc_server()
