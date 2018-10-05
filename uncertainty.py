#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), Mon Aug 27 12:00:54 2012
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
expName='unc_skeleton'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'001'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_uncertainty_%s' %(expInfo['participant'], expInfo['date'])
logFile=logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#an ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
datFile=open('data' + os.path.sep + '%s_uncertainty_%s.txt' %(expInfo['participant'], expInfo['date']),'a')
datFile.write('Trial\tRun\tpL/pR\tStim\tRorL\tstimOnset\trespRorL\tcorrectness\trespSize\tRT\n')

runNum=1
totRuns=5 #total runs plus 1 for practice
totStimNum=320 #not including practice, which always has 15
counterbalance = [0.95, 0.65, 0.35, 0.05]
seed(int(expInfo['participant'])+94)
shuffle(counterbalance)
while runNum<=totRuns:
    #setup the Window
    win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
        monitor=u'testMonitor', color=u'white', colorSpace=u'rgb')
    
    #Initialise components for Routine "instr"
    instrClock=core.Clock()
    text=visual.TextStim(win=win, ori=0, name='text',
        text='Please indicate whether the item is smaller (1 or 9) or larger (2 or 0) than a shoebox.\n\nIf you believe the item will reappear on the left side of the screen, respond with the 1 and 2 keys.\n\nIf you believe the item will reappear on the right side of the screen, respond with the 9 and 0 keys.\n\nPress enter to continue.',
        font='Arial',
        pos=[0, 0.2], height=0.1,wrapWidth=1.8,
        color='black', colorSpace='rgb', opacity=1,
        depth=0.0)
    begExpClock=core.Clock()
    
    #Initialise components for Routine "trial"
    trialClock=core.Clock()
    RTclock=core.Clock()
    
    
    image=visual.ImageStim(win=win, name='image',units=u'pix', 
        image='sin', mask=None,
        ori=0, pos=[0, 0], size=[256, 256],
        color=[1,1,1], colorSpace=u'rgb', opacity=1,
        texRes=128, interpolate=True, depth=-3.0)
    RorL=visual.TextStim(win=win, ori=0, name='RorL',
        text=u"1=smaller  2=larger             9=smaller  0=larger",
        font=u'Arial',
        pos=[0, -0.5], height=0.1,wrapWidth=3,
        color=u'black', colorSpace=u'rgb', opacity=1,
        depth=-5.0)
    fix1=visual.TextStim(win=win, ori=0, name='fix1',
        text=u'+',
        font=u'Arial',
        pos=[0, 0], height=0.1,wrapWidth=None,
        color=u'black', colorSpace=u'rgb', opacity=1,
        depth=-6.0)
    image_2=visual.ImageStim(win=win, name='image_2',units=u'pix', 
        image='sin', mask=None,
        ori=0, pos=[0,0], size=[256, 256],
        color=[1,1,1], colorSpace=u'rgb', opacity=1,
        texRes=128, interpolate=True, depth=-7.0)
    fix2=visual.TextStim(win=win, ori=0, name='fix2',
        text=u'+',
        font=u'Arial',
        pos=[0, 0], height=0.1,wrapWidth=None,
        color=u'black', colorSpace=u'rgb', opacity=1,
        depth=-8.0)
    
    # Create some handy timers
    globalClock=core.Clock() #to track the time since experiment started
    routineTimer=core.CountdownTimer() #to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine"instr"-------
    t=0; instrClock.reset() #clock 
    frameN=-1
    #update component parameters for each repeat
    key_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    key_resp.status=NOT_STARTED
    #keep track of which components have finished
    instrComponents=[]
    instrComponents.append(text)
    instrComponents.append(key_resp)
    for thisComponent in instrComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "instr"-------
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=instrClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*text* updates
        if t>=0.0 and text.status==NOT_STARTED:
            #keep track of start time/frame for later
            text.tStart=t#underestimates by a little under one frame
            text.frameNStart=frameN#exact frame index
            text.setAutoDraw(True)
        
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
            theseKeys = event.getKeys(keyList=['return'])
            if len(theseKeys)>0:#at least one key was pressed
                key_resp.keys=theseKeys[-1]#just the last key pressed
                key_resp.rt = key_resp.clock.getTime()
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
    begExpClock.reset()
    #set up handler to look after randomisation of conditions etc
    varLists=np.loadtxt('conditions.txt',dtype='str',delimiter='\t')  #loads info from conditions file (which should be a .txt not an .xlsx)
    stimList=varLists[:]  #chooses column for each category of data
    runLength=(totStimNum/(totRuns-1))
    lefts = []
    rights = []
    if runNum==1:
        pL=0.5
        pR=0.5
    elif runNum>1:
        pL=counterbalance[runNum-2]
        pR=(1-pL)
    for i in range(int(pL*len(varLists))):
        lefts.append([-256, 0])
    for i in range(int(pR*len(varLists))):
        rights.append([256, 0])
    direction = lefts + rights
    direction = np.asarray(direction)
    seed(int(expInfo['participant'])+65) #seeds randomization based on participant number
    shuffle(stimList)  #shuffles/randomizes list based on above seed
    seed(int(expInfo['participant'])+89) #seeds randomization based on participant number
    shuffle(direction)
    if runNum==1: #practice run
        currStims=stimList[(len(stimList)-10):len(stimList)] #picks the first 10 stims for practice round
        currDirection=direction[(len(stimList)-10):len(stimList)] #picks the first 10 stims for practice round
    elif runNum==2:
        currStims=stimList[0:runLength]  #picks a subset from the randomized list of total stims
        currDirection=direction[0:runLength]
    elif runNum>2:
        currStims=stimList[((runNum-2)*runLength):((runNum-1)*runLength)]
        currDirection=direction[0:runLength]

    print currDirection
    myarray = []
    for i in range(len(currStims)):
        myarray.append({'stim': currStims[i], 'pos': currDirection[i]}) #puts data into an array of dictionaries that the TrialHandler function will accept
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
#        durr1 = randint(3,8)
#        durr2 = randint(3,8)
        durr1=1
        durr2=2
        image.setImage(stim)
        key_resp_2 = event.BuilderKeyResponse() #create an object of type KeyResponse
        key_resp_2.status=NOT_STARTED
        image_2.setPos(pos)
        image_2.setImage(stim)
        #keep track of which components have finished
        trialComponents=[]
        trialComponents.append(image)
        trialComponents.append(key_resp_2)
        trialComponents.append(RorL)
        trialComponents.append(fix1)
        trialComponents.append(image_2)
        trialComponents.append(fix2)
        for thisComponent in trialComponents:
            if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
        #-------Start Routine "trial"-------
        continueRoutine=True
        while continueRoutine:
            #get current time
            t=trialClock.getTime()
            frameN=frameN+1#number of completed frames (so 0 in first frame)
            #update/draw components on each frame
            
            
            
            
            #*image* updates
            if t>=0.0 and image.status==NOT_STARTED:
                #keep track of start time/frame for later
                image.tStart=t#underestimates by a little under one frame
                image.frameNStart=frameN#exact frame index
                image.setAutoDraw(True)
                stimOn=begExpClock.getTime()
            elif image.status==STARTED and t>=(0.0+2):
                image.setAutoDraw(False)
            
            #*key_resp_2* updates
            if t>=0.0 and key_resp_2.status==NOT_STARTED:
                #keep track of start time/frame for later
                key_resp_2.tStart=t#underestimates by a little under one frame
                key_resp_2.frameNStart=frameN#exact frame index
                key_resp_2.status=STARTED
                #keyboard checking is just starting
                trialResponseTime='NaN'
                trialResponseKey=[]
                key_resp_2.clock.reset() # now t=0
                event.clearEvents()
                RTclock.reset()
            elif key_resp_2.status==STARTED and t>=(0.0+2):
                key_resp_2.status=STOPPED
            if key_resp_2.status==STARTED:#only update if being drawn
                theseKeys = event.getKeys(keyList=['1', '2', '9', '0'])
                if len(theseKeys)>0:#at least one key was pressed
                    key_resp_2.keys=theseKeys[-1]#just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    trialResponseTime=RTclock.getTime()
                    trialResponseKey=theseKeys[-1]
            
            #*RorL* updates
            if t>=0.0 and RorL.status==NOT_STARTED:
                #keep track of start time/frame for later
                RorL.tStart=t#underestimates by a little under one frame
                RorL.frameNStart=frameN#exact frame index
                RorL.setAutoDraw(True)
            elif RorL.status==STARTED and t>=(0.0+2):
                RorL.setAutoDraw(False)
            
            #*fix1* updates
            if t>=2 and fix1.status==NOT_STARTED:
                #keep track of start time/frame for later
                fix1.tStart=t#underestimates by a little under one frame
                fix1.frameNStart=frameN#exact frame index
                fix1.setAutoDraw(True)
            elif fix1.status==STARTED and t>=(2+durr1):
                fix1.setAutoDraw(False)
            
            #*image_2* updates
            if t>=(durr1+2) and image_2.status==NOT_STARTED:
                #keep track of start time/frame for later
                image_2.tStart=t#underestimates by a little under one frame
                image_2.frameNStart=frameN#exact frame index
                image_2.setAutoDraw(True)
            elif image_2.status==STARTED and t>=((durr1+2)+0.5):
                image_2.setAutoDraw(False)
            
            #*fix2* updates
            if t>=durr1+2.5 and fix2.status==NOT_STARTED:
                #keep track of start time/frame for later
                fix2.tStart=t#underestimates by a little under one frame
                fix2.frameNStart=frameN#exact frame index
                fix2.setAutoDraw(True)
            elif fix2.status==STARTED and t>=(durr1+2.5+durr2):
                fix2.setAutoDraw(False)
            
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
        if len(key_resp_2.keys)==0: #No response was made
           key_resp_2.keys=None
        #store data for trials (TrialHandler)
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:#we had a response
            trials.addData('key_resp_2.rt',key_resp_2.rt)
        thisExp.nextEntry()
    
    #completed 1 repeats of 'trials'
        if trialResponseKey==[]: #No response was made
           trialResponseKey=None
        trials.addData('respKey', trialResponseKey)
        if trialResponseKey != []:#we had a response
            trials.addData('RT',trialResponseTime)
        if any(pos==-256):
            location='L'
        elif any(pos==256):
            location='R'
        respLoc='None'
        respSize='None'
        if trialResponseKey=='1':
            respLoc='Left'
            respSize='Smaller'
        elif trialResponseKey=='2':
            respLoc='Left'
            respSize='Larger'
        elif trialResponseKey=='9':
            respLoc='Right'
            respSize='Smaller'
        elif trialResponseKey=='0':
            respLoc='Right'
            respSize='Larger'
        if location=='L' and respLoc=='Left':
            corr='correct'
        elif location=='R' and respLoc=='Right':
            corr='correct'
        else:
            corr='incorrect'
        datFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(trials.thisTrialN+1,runNum,'%s/%s',stim,location,stimOn,respLoc,corr,respSize,trialResponseTime)%(pL,pR))
#    get names of stimulus parameters
    if trials.trialList in ([], [None], None):  params=[]
    else:  params = trials.trialList[0].keys()
    runNum=runNum+1


#save data for this loop
#trials.saveAsPickle(filename+'trials', fileCollisionMethod='rename')
#trials.saveAsExcel(filename+'.xlsx', sheetName='trials',
#    stimOut=params,
#    dataOut=['n','all_mean','all_std', 'all_raw'])

#Shutting down:
win.close()
core.quit()
