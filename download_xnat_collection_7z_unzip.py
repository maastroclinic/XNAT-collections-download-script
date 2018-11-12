# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 07:41:00 2017

@author: leonard.wee
"""


#this needs the xnat package installed i.e.
#pip install xnat
import xnat
import os
import subprocess


myWorkingDirectory = 'C:\\Nature2018' #edit the working directory to where you want the downloaded zips to land
collectionURL = 'https://xnat.bmia.nl' #edit this if you are using a different XNAT repo
myProjectID = 'stwstrategymmd' #edit this for the collection you want to download


# Download data from XNAT in .zip format
def xnat_collection(myWorkingDirectory,collectionURL,myProjectID):
    os.chdir(myWorkingDirectory)
    #connections to public collections do not require passwords
    with xnat.connect(collectionURL) as mySession:
        myProject= mySession.projects[myProjectID]
        mySubjectsList = myProject.subjects.values()
        for s in mySubjectsList:
            mySubjectID = s.label
            print('\nEntering subject ...' + mySubjectID)
            mySubject = myProject.subjects[mySubjectID]
            myExperimentsList = mySubject.experiments.values()
            for e in myExperimentsList:
                myExperimentID = e.label
                #print('\nEntering experiment ...' + myExperimentID)
                myExperiment = mySubject.experiments[myExperimentID]
                #the next line downloads each subject, experiment pair one-by-one into separate zip files
                #myExperiment.download(myWorkingDirectory + '\\' + myProjectID + '_' + mySubjectID + '_' + myExperimentID + '.zip')
                myExperiment.download(myWorkingDirectory + '\\' + myExperimentID + '.zip')
    return
#
#
#
xnat_collection(myWorkingDirectory,collectionURL,myProjectID)
# Unzip zip files download from XNAT
archives = [fn for fn in os.listdir('.') if fn.endswith('.zip')]
for zipname in archives:
    print ("processing ... " + zipname)
    subprocess.call(r'"C:\Program Files\7-Zip\7z.exe" x ' + zipname + ' -o' + myProjectID)

