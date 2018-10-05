#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), Wed May 29 13:24:25 2013
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division #so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import * #things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle, seed
import os #handy system and path functions

#store info about the experiment session
expName='None'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'f'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_%s_%s' %(expInfo['participant'], expInfo['session'], expInfo['date'])
logFile=logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#an ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=True,
    dataFileName=filename)
datFile=open('data' + os.path.sep + '%s_%s_SART.txt' %(expInfo['participant'], expInfo['session']),'a')
datFile.write('Trial\tDigit\tRunType\tResponse\tGoHits\tNogoHits\tCommissions\tOmissions\tstimOnset\tRT\n')

#setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'white', colorSpace=u'rgb')

#Initialise components for Routine "scan"
scanClock=core.Clock()
wait=visual.TextStim(win=win, ori=0, name='wait',
    text='Please respond to the bolded cue after every digit except "3"\n\nWaiting for scanner...',
    font=u'Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=0.0)

#Initialise components for Routine "trial"
trialClock=core.Clock()
digit=visual.TextStim(win=win, ori=0, name='digit',
    text='nonsense',
    font=u'Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=0.0)
mask1=visual.PatchStim(win=win, name='mask1',units=u'pix',
    tex=u'mask.png', mask=None,
    ori=0, pos=[0, 0], size=[256,256], sf=None, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=False, depth=-1.0)
response_cue=visual.PatchStim(win=win, name='response_cue',units=u'pix',
    tex=u'resp_cue.png', mask=None,
    ori=0, pos=[0, 0], size=[256,256], sf=None, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=False, depth=-2.0)
mask2=visual.PatchStim(win=win, name='mask2',units=u'pix',
    tex=u'mask.png', mask=None,
    ori=0, pos=[0, 0], size=[256,256], sf=None, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=False, depth=-3.0)
fixation=visual.PatchStim(win=win, name='fixation',units=u'pix',
    tex=u'fixation.png', mask=None,
    ori=0, pos=[0, 0], size=[256,256], sf=None, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=False, depth=-4.0)

# Create some handy timers
globalClock=core.Clock() #to track the time since experiment started
routineTimer=core.CountdownTimer() #to track time remaining of each (non-slip) routine 
begExpClock=core.Clock() #to track the time since the actual paradigm started (after the scanner screen)

#------Prepare to start Routine"scan"-------
t=0; scanClock.reset() #clock 
frameN=-1
#update component parameters for each repeat
scan_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
scan_resp.status=NOT_STARTED
#keep track of which components have finished
scanComponents=[]
scanComponents.append(wait)
scanComponents.append(scan_resp)
for thisComponent in scanComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#-------Start Routine "scan"-------
continueRoutine=True
while continueRoutine:
    #get current time
    t=scanClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*wait* updates
    if t>=0.0 and wait.status==NOT_STARTED:
        #keep track of start time/frame for later
        wait.tStart=t#underestimates by a little under one frame
        wait.frameNStart=frameN#exact frame index
        wait.setAutoDraw(True)
    
    #*scan_resp* updates
    if t>=0.0 and scan_resp.status==NOT_STARTED:
        #keep track of start time/frame for later
        scan_resp.tStart=t#underestimates by a little under one frame
        scan_resp.frameNStart=frameN#exact frame index
        scan_resp.status=STARTED
        #keyboard checking is just starting
        scan_resp.clock.reset() # now t=0
        event.clearEvents()
    if scan_resp.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['+', 'num_add', 'return'])
        if len(theseKeys)>0:#at least one key was pressed
            scan_resp.keys=theseKeys[-1]#just the last key pressed
            scan_resp.rt = scan_resp.clock.getTime()
            #abort routine on response
            continueRoutine=False
    
    #check if all components have finished
    if not continueRoutine: #a component has requested that we end
        routineTimer.reset() #this is the new t0 for non-slip Routines
        break
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in scanComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#End of Routine "scan"
for thisComponent in scanComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#set up handler to look after randomisation of conditions etc
trialNum=25
set=[1,2,3,4,5,6,7,8,9]
if expInfo['session']=='f': #fixed
    digits=set*trialNum
elif expInfo['session']=='r': #random
    digits=[]
    for i in range(trialNum):
        seed(i)
        shuffle(set)
        digits.extend(set)
    for i in range(len(digits)): #makes sure that there are never two consecutive 'nogo' trials
        if digits[i]==3 and digits[i-1]==3:
            temp=digits[i+1]
            digits[i]=temp
            digits[i+1]=3
myarray = []
for i in range(len(digits)):
    myarray.append({'digits': digits[i]}) #puts data into an array of dictionaries that the TrialHandler function will accept
trials=data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=myarray,
    seed=None, name='trials')
thisExp.addLoop(trials)#add the loop to the experiment
thisTrial=trials.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial!=None:
    for paramName in thisTrial.keys():
        exec(paramName+'=thisTrial.'+paramName)
begExpClock.reset()
for thisTrial in trials:
    currentLoop = trials
    #abbrieviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial!=None:
        for paramName in thisTrial.keys():
            exec(paramName+'=thisTrial.'+paramName)
    
    #------Prepare to start Routine"trial"-------
    t=0; trialClock.reset() #clock 
    frameN=-1
    routineTimer.add(1.439000)
    #update component parameters for each repeat
    digit.setText(digits)
    key_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    key_resp.status=NOT_STARTED
    #keep track of which components have finished
    trialComponents=[]
    trialComponents.append(digit)
    trialComponents.append(mask1)
    trialComponents.append(response_cue)
    trialComponents.append(mask2)
    trialComponents.append(fixation)
    trialComponents.append(key_resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "trial"-------
    continueRoutine=True
    while continueRoutine and routineTimer.getTime()>0:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*digit* updates
        if t>=0.0 and digit.status==NOT_STARTED:
            #keep track of start time/frame for later
            digit.tStart=t#underestimates by a little under one frame
            digit.frameNStart=frameN#exact frame index
            digit.setAutoDraw(True)
            stimOn=begExpClock.getTime()
        elif digit.status==STARTED and t>=(0.0+0.313):
            digit.setAutoDraw(False)
        
        #*mask1* updates
        if t>=0.313 and mask1.status==NOT_STARTED:
            #keep track of start time/frame for later
            mask1.tStart=t#underestimates by a little under one frame
            mask1.frameNStart=frameN#exact frame index
            mask1.setAutoDraw(True)
        elif mask1.status==STARTED and t>=(0.313+0.125):
            mask1.setAutoDraw(False)
        
        #*response_cue* updates
        if t>=0.438 and response_cue.status==NOT_STARTED:
            #keep track of start time/frame for later
            response_cue.tStart=t#underestimates by a little under one frame
            response_cue.frameNStart=frameN#exact frame index
            response_cue.setAutoDraw(True)
        elif response_cue.status==STARTED and t>=(0.438+0.063):
            response_cue.setAutoDraw(False)
        
        #*mask2* updates
        if t>=0.501 and mask2.status==NOT_STARTED:
            #keep track of start time/frame for later
            mask2.tStart=t#underestimates by a little under one frame
            mask2.frameNStart=frameN#exact frame index
            mask2.setAutoDraw(True)
        elif mask2.status==STARTED and t>=(0.501+0.375):
            mask2.setAutoDraw(False)
        
        #*fixation* updates
        if t>=0.876 and fixation.status==NOT_STARTED:
            #keep track of start time/frame for later
            fixation.tStart=t#underestimates by a little under one frame
            fixation.frameNStart=frameN#exact frame index
            fixation.setAutoDraw(True)
        elif fixation.status==STARTED and t>=(0.876+0.563):
            fixation.setAutoDraw(False)
        
        #*key_resp* updates
        if t>=0 and key_resp.status==NOT_STARTED:
            #keep track of start time/frame for later
            key_resp.tStart=t#underestimates by a little under one frame
            key_resp.frameNStart=frameN#exact frame index
            key_resp.status=STARTED
            #keyboard checking is just starting
            key_resp.clock.reset() # now t=0
            event.clearEvents()
        elif key_resp.status==STARTED and t>=(0+1.439):
            key_resp.status=STOPPED
        if key_resp.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['1'])
            if len(theseKeys)>0:#at least one key was pressed
                key_resp.keys=theseKeys[-1]#just the last key pressed
                key_resp.rt = key_resp.clock.getTime()
        
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
    if digits!=3 and key_resp.keys=='1':
        [Ghit,Nhit,CE,OE]=[1,0,0,0]
    elif digits==3 and key_resp.keys==None:
        [Ghit,Nhit,CE,OE]=[0,1,0,0]
    elif digits==3 and key_resp.keys=='1':
        [Ghit,Nhit,CE,OE]=[0,0,1,0]
    elif digits!=3 and key_resp.keys==None:
        [Ghit,Nhit,CE,OE]=[0,0,0,1]
    datFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(trials.thisTrialN+1,digits,expInfo['session'],key_resp.keys,Ghit,Nhit,CE,OE,stimOn,key_resp.rt))

#save data for this loop
#trials.saveAsPickle(filename+'trials', fileCollisionMethod='rename')

#Shutting down:
win.close()
core.quit()
