#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), Mon Jul 30 11:05:40 2012
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division #so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import * #things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
from random import seed, shuffle
import os #handy system and path functions

#store info about the experiment session
expName='None'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'001'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_ret_%s' %(expInfo['participant'], expInfo['date'])
logFile=logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#an ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

datFile=open('data' + os.path.sep + '%s_%s.txt' %(expInfo['participant'], expInfo['date']),'w')
datFile.write('Trial\tStim\tOldvsNew\tResp\tRT\tAcc\tHit\tMiss\tFA\tCR\n')


#setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace=u'rgb')

#Initialise components for Routine "instr"
instrClock=core.Clock()
instructions=visual.TextStim(win=win, ori=0, name='instructions',
    text=u"Press '1' if the image is old, press '2' if the image is familiar, and press '3' if the image is new. Press the 'return' key to begin.",
    font=u'Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

#Initialise components for Routine "trial"
trialClock=core.Clock()
text=visual.TextStim(win=win, ori=0, name='text',
    text=u'old=1    familiar=2    new=3',
    font=u'Arial',
    pos=[0, -0.5], height=0.1,wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
image=visual.ImageStim(win=win, name='image',units=u'pix',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[225, 338],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)

# Create some handy timers
globalClock=core.Clock() #to track the time since experiment started
routineTimer=core.CountdownTimer() #to track time remaining of each (non-slip) routine 

#------Prepare to start Routine"instr"-------
t=0; instrClock.reset() #clock 
frameN=-1
#update component parameters for each repeat
key_start = event.BuilderKeyResponse() #create an object of type KeyResponse
key_start.status=NOT_STARTED
#keep track of which components have finished
instrComponents=[]
instrComponents.append(instructions)
instrComponents.append(key_start)
for thisComponent in instrComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#-------Start Routine "instr"-------
continueRoutine=True
while continueRoutine:
    #get current time
    t=instrClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*instructions* updates
    if t>=0.0 and instructions.status==NOT_STARTED:
        #keep track of start time/frame for later
        instructions.tStart=t#underestimates by a little under one frame
        instructions.frameNStart=frameN#exact frame index
        instructions.setAutoDraw(True)
    
    #*key_start* updates
    if t>=0.0 and key_start.status==NOT_STARTED:
        #keep track of start time/frame for later
        key_start.tStart=t#underestimates by a little under one frame
        key_start.frameNStart=frameN#exact frame index
        key_start.status=STARTED
        #keyboard checking is just starting
        key_start.clock.reset() # now t=0
        event.clearEvents()
    if key_start.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys)>0:#at least one key was pressed
            key_start.keys=theseKeys[-1]#just the last key pressed
            key_start.rt = key_start.clock.getTime()
            #abort routine on response
            continueRoutine=False
    
    #check if all components have finished
    if not continueRoutine: #a component has requested that we end
        routineTimer.reset() #this is the new t0 for non-slip Routines
        break
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#End of Routine "instr"
for thisComponent in instrComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#re-establish stim order of encoding so we can later determine what was old and new **Note: want to make sure that this randomization code stays consistent with that in the encoding script**
stimLists=np.loadtxt('conditions3.txt',dtype='str',delimiter='\t')  #loads info from conditions file (which should be a .txt not an .xlsx)
faceList=stimLists[:,0]
sceneList=stimLists[:,1]
seed(int(expInfo['participant'])+65) #seeds randomization based on participant number
shuffle(faceList)  #shuffles/randomizes list based on above seed
seed(int(expInfo['participant'])+43) #seeds randomization based on participant number
shuffle(sceneList)
totStimNumOld=120
totRunsOld=6
faces_old=faceList[0:totStimNumOld] #picks the first 120 from the randomized list of total faces/scenes
scenes_old=sceneList[0:totStimNumOld]
runLength=(totStimNumOld/totRunsOld)
run1_faces=faceList[0:runLength]
run2_faces=faceList[runLength:(runLength*2)]
run3_faces=faceList[(runLength*2):(runLength*3)]
run4_faces=faceList[(runLength*3):(runLength*4)]
run5_faces=faceList[(runLength*4):(runLength*5)]
run6_faces=faceList[(runLength*5):(runLength*6)]
run1_scenes=sceneList[0:runLength]
run2_scenes=sceneList[runLength:(runLength*2)]
run3_scenes=sceneList[(runLength*2):(runLength*3)]
run4_scenes=sceneList[(runLength*3):(runLength*4)]
run5_scenes=sceneList[(runLength*4):(runLength*5)]
run6_scenes=sceneList[(runLength*5):(runLength*6)]
stimList_ret= np.hstack((faceList,sceneList))
myarray = []
for i in range(len(stimList_ret)):
    myarray.append({'stims': stimList_ret[i]}) #puts data into an array of dictionaries that the TrialHandler function will accept

#set up handler to look after randomisation of conditions etc
trials=data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=myarray,
    seed=(int(expInfo['participant'])+71), name='trials')
thisExp.addLoop(trials)#add the loop to the experiment
thisTrial=trials.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial!=None:
    for paramName in thisTrial.keys():
        exec(paramName+'=thisTrial.'+paramName)

for thisTrial in trials:
    currentLoop = trials
    #abbrieviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial!=None:
        for paramName in thisTrial.keys():
            exec(paramName+'=thisTrial.'+paramName)
    
    #------Prepare to start Routine"trial"-------
    t=0; trialClock.reset() #clock 
    frameN=-1
    #update component parameters for each repeat
    key_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    key_resp.status=NOT_STARTED
    image.setImage(stims)
    #keep track of which components have finished
    trialComponents=[]
    trialComponents.append(key_resp)
    trialComponents.append(text)
    trialComponents.append(image)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "trial"-------
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*key_resp* updates
        if t>=0.0 and key_resp.status==NOT_STARTED:
            #keep track of start time/frame for later
            key_resp.tStart=t#underestimates by a little under one frame
            key_resp.frameNStart=frameN#exact frame index
            key_resp.status=STARTED
            #keyboard checking is just starting
            key_resp.clock.reset() # now t=0
            event.clearEvents()
        if key_resp.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['1', '2', '3'])
            if len(theseKeys)>0:#at least one key was pressed
                key_resp.keys=theseKeys[-1]#just the last key pressed
                key_resp.rt = key_resp.clock.getTime()
                #abort routine on response
                continueRoutine=False
        
        #*text* updates
        if t>=0.0 and text.status==NOT_STARTED:
            #keep track of start time/frame for later
            text.tStart=t#underestimates by a little under one frame
            text.frameNStart=frameN#exact frame index
            text.setAutoDraw(True)
        
        #*image* updates
        if t>=0.0 and image.status==NOT_STARTED:
            #keep track of start time/frame for later
            image.tStart=t#underestimates by a little under one frame
            image.frameNStart=frameN#exact frame index
            image.setAutoDraw(True)
        
        #check if all components have finished
        if not continueRoutine: #a component has requested that we end
            routineTimer.reset() #this is the new t0 for non-slip Routines
            break
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #End of Routine "trial"
    for thisComponent in trialComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    #check responses
    if len(key_resp.keys)==0: #No response was made
       key_resp.keys=None
    #store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:#we had a response
        trials.addData('key_resp.rt',key_resp.rt)
    thisExp.nextEntry()

#completed 1 repeats of 'trials'
#    trials.addData('stimOnset',fixOff)
#    datFile.write('%s\t%s\t%s\t%s\t%s\n'%(trials.thisTrialN+1,thisTrial.faces,thisTrial.scenes,fixOff,trialResponseTime))
#creating all the variables needed for the log file and writing them to this log file
    if any(stims==faces_old) or any(stims==scenes_old):
        oldornew=1
    else:
        oldornew=0
    if oldornew==1 and key_resp.keys=='1':
        hits=1
    elif oldornew==1 and key_resp.keys=='2':
        hits=1
    else:
        hits=0
    if oldornew==1 and key_resp.keys=='3':
        misses=1
    else:
        misses=0
    if oldornew==0 and key_resp.keys=='1':
        FAs=1
    elif oldornew==0 and key_resp.keys=='2':
        FAs=1
    else:
        FAs=0
    if oldornew==0 and key_resp.keys=='3':
        CRs=1
    else:
        CRs=0
    if hits==1 or CRs==1:
        Acc=1
    else:
        Acc=0
    trials.addData('OldvsNew',oldornew)
    trials.addData('Hit',hits)
    trials.addData('misses',misses)
    trials.addData('FAs',FAs)
    trials.addData('CRs',CRs)
    trials.addData('Acc',Acc)
    datFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(trials.thisTrialN+1,stims,oldornew,key_resp.keys,key_resp.rt,Acc,hits,misses,FAs,CRs))

datFile.close()

#get names of stimulus parameters
if trials.trialList in ([], [None], None):  params=[]
else:  params = trials.trialList[0].keys()
#save data for this loop
trials.saveAsPickle(filename+'trials', fileCollisionMethod='rename')
trials.saveAsExcel(filename+'.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#Shutting down:
win.close()
core.quit()
