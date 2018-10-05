#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), Fri May 24 16:40:14 2013
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
expName='n-back_skeleton'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'1'}
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
datFile=open('data' + os.path.sep + '%s_%s_n-back.txt' %(expInfo['participant'], expInfo['session']),'a')
datFile.write('Trial\tBlockNum\tRun\tn-back\tResponse\tTargets\tHits\tMisses\tFAs\tCRs\tstimOnset\tRT\tposition\tInstructionOnset\n')

#setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace=u'rgb')

#Initialise components for Routine "scanner"
scannerClock=core.Clock()
waiting=visual.TextStim(win=win, ori=0, name='waiting',
    text='Waiting for scanner...',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

#Initialise components for Routine "instr"
instrClock=core.Clock()
instructions=visual.TextStim(win=win, ori=0, name='instructions',
    text='nonsense',
    font=u'Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

#Initialise components for Routine "trial"
trialClock=core.Clock()
square=visual.PatchStim(win=win, name='square',
    tex='sqr', mask=None,
    ori=0, pos=[0,0], size=[0.1, 0.1], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

#Initialise components for Routine "rest"
restClock=core.Clock()
fix=visual.TextStim(win=win, ori=0, name='fix',
    text=u'+',
    font=u'Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock=core.Clock() #to track the time since experiment started
routineTimer=core.CountdownTimer() #to track time remaining of each (non-slip) routine 
begExpClock=core.Clock() #to track the time since the actual paradigm started (after the 'Wating for scanner' screen)

#------Prepare to start Routine"scanner"-------
t=0; scannerClock.reset() #clock 
frameN=-1
#update component parameters for each repeat
sync_pulse = event.BuilderKeyResponse() #create an object of type KeyResponse
sync_pulse.status=NOT_STARTED
#keep track of which components have finished
scannerComponents=[]
scannerComponents.append(waiting)
scannerComponents.append(sync_pulse)
for thisComponent in scannerComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#-------Start Routine "scanner"-------
continueRoutine=True
while continueRoutine:
    #get current time
    t=scannerClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*waiting* updates
    if t>=0.0 and waiting.status==NOT_STARTED:
        #keep track of start time/frame for later
        waiting.tStart=t#underestimates by a little under one frame
        waiting.frameNStart=frameN#exact frame index
        waiting.setAutoDraw(True)
    
    #*sync_pulse* updates
    if t>=0.0 and sync_pulse.status==NOT_STARTED:
        #keep track of start time/frame for later
        sync_pulse.tStart=t#underestimates by a little under one frame
        sync_pulse.frameNStart=frameN#exact frame index
        sync_pulse.status=STARTED
        #keyboard checking is just starting
        sync_pulse.clock.reset() # now t=0
        event.clearEvents()
    if sync_pulse.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['+', 'num_add', 'return'])
        if len(theseKeys)>0:#at least one key was pressed
            sync_pulse.keys=theseKeys[-1]#just the last key pressed
            sync_pulse.rt = sync_pulse.clock.getTime()
            #abort routine on response
            continueRoutine=False
    
    #check if all components have finished
    if not continueRoutine: #a component has requested that we end
        routineTimer.reset() #this is the new t0 for non-slip Routines
        break
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in scannerComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#End of Routine "scanner"
for thisComponent in scannerComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#set up handler to look after randomisation of conditions etc
if expInfo['session']=='1':
    run=[1,2,1,2,2,1,2,1,1]
elif expInfo['session']=='2':
    run=[2,2,1,1,1,2,2,1,2]
myarray = []
for i in range(len(run)):
    myarray.append({'run': run[i], 'runNum': (i)}) #puts data into an array of dictionaries that the TrialHandler function will accept
block=data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=myarray,
    seed=None, name='block')
thisExp.addLoop(block)#add the loop to the experiment
thisBlock=block.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisBlock.rgb)
if thisBlock!=None:
    for paramName in thisBlock.keys():
        exec(paramName+'=thisBlock.'+paramName)
begExpClock.reset()
for thisBlock in block:
    currentLoop = block
    #abbrieviate parameter names if possible (e.g. rgb=thisBlock.rgb)
    if thisBlock!=None:
        for paramName in thisBlock.keys():
            exec(paramName+'=thisBlock.'+paramName)
    
    #------Prepare to start Routine"instr"-------
    t=0; instrClock.reset() #clock 
    frameN=-1
    routineTimer.add(2.000000)
    #update component parameters for each repeat
    instructions.setText(u"This is a %s-back"%(run))
    #keep track of which components have finished
    instrComponents=[]
    instrComponents.append(instructions)
    for thisComponent in instrComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "instr"-------
    continueRoutine=True
    while continueRoutine and routineTimer.getTime()>0:
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
            instrOn=begExpClock.getTime()
        elif instructions.status==STARTED and t>=(0.0+2.0):
            instructions.setAutoDraw(False)
        
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
    
    #set up handler to look after randomisation of conditions etc
    allPos=[[0,0.75],[0.257, 0.705],[0.482,0.575],[0.65,0.375],[0.739,0.13],[0.739,-0.13],[0.65,-0.375],[0.482,-0.575],[0.257,-0.705],[0,-0.75],[-0.257, 0.705],[-0.482,0.575],[-0.65,0.375],[-0.739,0.13],[-0.739,-0.13],[-0.65,-0.375],[-0.482,-0.575],[-0.257,-0.705]]
    if expInfo['session']=='1':
        allOrders=[[0,1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],[0,0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],[0,0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0]]
        #123,231,213
        seed(runNum)
        shuffle(allPos)
    elif expInfo['session']=='2':
        allOrders=[[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],[0,0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],[0,1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],[0,0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0]]
        #321,132,312
        seed(runNum+42)
        shuffle(allPos)
    order=allOrders[runNum]
    position=[]
    if run==1:
        for i in range(len(order)):
            if order[i]==0:
                position.append(allPos[i])
            elif order[i]==1:
                position.append(allPos[i-1])
    elif run==2:
        for i in range(len(order)):
            if order[i]==0:
                position.append(allPos[i])
            elif order[i]==1:
                position.append(allPos[i-2])
    elif run==3:
        for i in range(len(order)):
            if order[i]==0:
                position.append(allPos[i])
            elif order[i]==1:
                position.append(allPos[i-3])
    print position
    myarray = []
    for i in range(len(position)):
        myarray.append({'pos': position[i], 'order': order[i]}) #puts data into an array of dictionaries that the TrialHandler function will accept
    trials=data.TrialHandler(nReps=1, method='sequential', 
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
        routineTimer.add(2.000000)
        #update component parameters for each repeat
        square.setPos(pos)
        key_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
        key_resp.status=NOT_STARTED
        #keep track of which components have finished
        trialComponents=[]
        trialComponents.append(square)
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
            
            #*square* updates
            if t>=0.0 and square.status==NOT_STARTED:
                #keep track of start time/frame for later
                square.tStart=t#underestimates by a little under one frame
                square.frameNStart=frameN#exact frame index
                square.setAutoDraw(True)
                stimOn=begExpClock.getTime()
            elif square.status==STARTED and t>=(0.0+0.5):
                square.setAutoDraw(False)
            
            #*key_resp* updates
            if t>=0.0 and key_resp.status==NOT_STARTED:
                #keep track of start time/frame for later
                key_resp.tStart=t#underestimates by a little under one frame
                key_resp.frameNStart=frameN#exact frame index
                key_resp.status=STARTED
                #keyboard checking is just starting
                key_resp.clock.reset() # now t=0
                event.clearEvents()
            elif key_resp.status==STARTED and t>=(0.0+2.0):
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
        if order==1 and key_resp.keys=='1':
            [hit,miss,FA,CR]=[1,0,0,0]
        elif order==0 and key_resp.keys=='1':
            [hit,miss,FA,CR]=[0,0,1,0]
        elif order==1 and key_resp.keys==None:
            [hit,miss,FA,CR]=[0,1,0,0]
        elif order==0 and key_resp.keys==None:
            [hit,miss,FA,CR]=[0,0,0,1]
        datFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(trials.thisTrialN+1,runNum+1,expInfo['session'],run,key_resp.keys,order,hit,miss,FA,CR,stimOn,key_resp.rt,pos,instrOn))
#        print 'trial=%s,block=%s,run=%s,n-back=%s,resp=%s,targ=%s,RT=%s'%(trials.thisTrialN+1,runNum+1,expInfo['session'],run,key_resp.keys,order,key_resp.rt)
    #save data for this loop
#    trials.saveAsPickle(filename+'trials', fileCollisionMethod='rename')
    
    #------Prepare to start Routine"rest"-------
    t=0; restClock.reset() #clock 
    frameN=-1
    routineTimer.add(15.000000)
#    routineTimer.add(3.000000)
    #update component parameters for each repeat
    #keep track of which components have finished
    restComponents=[]
    restComponents.append(fix)
    for thisComponent in restComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "rest"-------
    continueRoutine=True
    while continueRoutine and routineTimer.getTime()>0:
        #get current time
        t=restClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*fix* updates
        if t>=0.0 and fix.status==NOT_STARTED:
            #keep track of start time/frame for later
            fix.tStart=t#underestimates by a little under one frame
            fix.frameNStart=frameN#exact frame index
            fix.setAutoDraw(True)
        elif fix.status==STARTED and t>=(0.0+15.0):
            fix.setAutoDraw(False)
        
        #check if all components have finished
        if not continueRoutine: #a component has requested that we end
            routineTimer.reset() #this is the new t0 for non-slip Routines
            break
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #End of Routine "rest"
    for thisComponent in restComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    thisExp.nextEntry()

#completed 1 repeats of 'block'


#save data for this loop
#block.saveAsPickle(filename+'block', fileCollisionMethod='rename')

#Shutting down:
win.close()
core.quit()
