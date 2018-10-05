#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), Thu Aug 22 17:37:08 2013
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
expInfo={'participant':'', 'run':'1'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile=logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#an ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=False,
    dataFileName=filename)
datFile=open('data' + os.path.sep + '%s_dyn_run%s.txt' %(expInfo['participant'], expInfo['run']),'a')
datFile.write('Trial\tStim\tType\tOnset\n')

#setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace=u'rgb')

#Initialise components for Routine "waiting"
waitingClock=core.Clock()
circles=visual.MovieStim(win=win, name='circles',units=u'norm', 
    filename=u'stimuli/oblique1.mov',
    ori=0, pos=[0, 0], opacity=1, loop=True,
    size=2,
    depth=0.0,
    )

#Initialise components for Routine "fix"
fixClock=core.Clock()
fullscreen=visual.GratingStim(win=win, name='fullscreen',units=u'norm', 
    tex=None, mask=None,
    ori=0, pos=[0, 0], size=2, sf=None, phase=0.0,
    color=1.0, colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

#Initialise components for Routine "trial"
trialClock=core.Clock()

# Create some handy timers
globalClock=core.Clock() #to track the time since experiment started
routineTimer=core.CountdownTimer() #to track time remaining of each (non-slip) routine 
begExpClock=core.Clock() #to track the time since the waiting routine ended (ie when the sync pulse was given)

#------Prepare to start Routine"waiting"-------
t=0; waitingClock.reset() #clock 
frameN=-1
#update component parameters for each repeat
scan_start = event.BuilderKeyResponse() #create an object of type KeyResponse
scan_start.status=NOT_STARTED
#keep track of which components have finished
waitingComponents=[]
waitingComponents.append(circles)
waitingComponents.append(scan_start)
for thisComponent in waitingComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#-------Start Routine "waiting"-------
continueRoutine=True
while continueRoutine:
    #get current time
    t=waitingClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*circles* updates
    if t>=0.0 and circles.status==NOT_STARTED:
        #keep track of start time/frame for later
        circles.tStart=t#underestimates by a little under one frame
        circles.frameNStart=frameN#exact frame index
        circles.setAutoDraw(True)
    
    #*scan_start* updates
    if t>=0.0 and scan_start.status==NOT_STARTED:
        #keep track of start time/frame for later
        scan_start.tStart=t#underestimates by a little under one frame
        scan_start.frameNStart=frameN#exact frame index
        scan_start.status=STARTED
        #keyboard checking is just starting
        scan_start.clock.reset() # now t=0
        event.clearEvents()
    if scan_start.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['return', '+', 'num_add'])
        if len(theseKeys)>0:#at least one key was pressed
            scan_start.keys=theseKeys[-1]#just the last key pressed
            scan_start.rt = scan_start.clock.getTime()
            #abort routine on response
            continueRoutine=False
    
    #check if all components have finished
    if not continueRoutine: #a component has requested that we end
        routineTimer.reset() #this is the new t0 for non-slip Routines
        break
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in waitingComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#End of Routine "waiting"
for thisComponent in waitingComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
begExpClock.reset()

rep=0
while rep<2:
    #set up handler to look after randomisation of conditions etc
    allColors=np.array(['darkgreen','red','blue','yellow','orange','lime','brown','cyan','purple','violet'])
    myarray = []
    for i in range(6):
        myarray.append({'color': allColors[i]}) #puts data into an array of dictionaries that the TrialHandler function will accept
    fixes=data.TrialHandler(nReps=1, method=u'random', 
        extraInfo=expInfo, originPath=None,
        trialList=myarray,
        seed=None, name='fixes')
    thisExp.addLoop(fixes)#add the loop to the experiment
    thisFixe=fixes.trialList[0]#so we can initialise stimuli with some values
    #abbreviate parameter names if possible (e.g. rgb=thisFixe.rgb)
    if thisFixe!=None:
        for paramName in thisFixe.keys():
            exec(paramName+'=thisFixe.'+paramName)
    
    for thisFixe in fixes:
        currentLoop = fixes
        #abbrieviate parameter names if possible (e.g. rgb=thisFixe.rgb)
        if thisFixe!=None:
            for paramName in thisFixe.keys():
                exec(paramName+'=thisFixe.'+paramName)
        
        #------Prepare to start Routine"fix"-------
        t=0; fixClock.reset() #clock 
        frameN=-1
        routineTimer.add(3.000000)
        #update component parameters for each repeat
        fullscreen.setColor(color, colorSpace=u'rgb')
        #keep track of which components have finished
        fixComponents=[]
        fixComponents.append(fullscreen)
        for thisComponent in fixComponents:
            if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
        #-------Start Routine "fix"-------
        continueRoutine=True
        while continueRoutine and routineTimer.getTime()>0:
            #get current time
            t=fixClock.getTime()
            frameN=frameN+1#number of completed frames (so 0 in first frame)
            #update/draw components on each frame
            
            #*fullscreen* updates
            if t>=0.0 and fullscreen.status==NOT_STARTED:
                #keep track of start time/frame for later
                fullscreen.tStart=t#underestimates by a little under one frame
                fullscreen.frameNStart=frameN#exact frame index
                fullscreen.setAutoDraw(True)
            elif fullscreen.status==STARTED and t>=(0.0+3.0):
                fullscreen.setAutoDraw(False)
            
            #check if all components have finished
            if not continueRoutine: #a component has requested that we end
                routineTimer.reset() #this is the new t0 for non-slip Routines
                break
            continueRoutine=False#will revert to True if at least one component still running
            for thisComponent in fixComponents:
                if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                    continueRoutine=True; break#at least one component has not yet finished
            
            #check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            #refresh the screen
            if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #End of Routine "fix"
        for thisComponent in fixComponents:
            if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
    
    #completed 1 repeats of 'fixes'
    
    
    #set up handler to look after randomisation of conditions etc
    allstims=np.genfromtxt('conditions.txt',dtype=str,delimiter='\t',skip_header=1)
    allBodies=allstims[:,0]
    allFaces=allstims[:,1]
    allObjects=allstims[:,2]
    allScenes=allstims[:,3]
    allScrambled=allstims[:,4]
    seed(int(expInfo['participant'])+int(expInfo['run'])+65)
    shuffle(allBodies)
    shuffle(allFaces)
    shuffle(allObjects)
    shuffle(allScenes)
    shuffle(allScrambled)
    if rep==0:
        ran=range(6)
        blockNum=range(5)
    elif rep==1:
        ran=range(6,12)
        blockNum=range(5,10)
    designs = [[1,2,3,4,5,5,4,3,2,1],[2,4,1,3,5,5,3,1,4,2],[3,2,5,1,4,4,1,5,2,3],[4,1,5,2,3,3,2,5,1,4],[5,3,1,4,2,2,4,1,3,5],[5,4,3,2,1,1,2,3,4,5]]
    blockList=np.array(designs[int(expInfo['run'])-1])
    stimList=[]
    typeList=[]
    for block in blockList[blockNum]:
        if block ==1:
            stimList.extend(allFaces[ran])
            typeList.extend(['face']*len(ran))
        elif block==2:
            stimList.extend(allBodies[ran])
            typeList.extend(['body']*len(ran))
        elif block==3:
            stimList.extend(allScenes[ran])
            typeList.extend(['scene']*len(ran))
        elif block==4:
            stimList.extend(allObjects[ran])
            typeList.extend(['object']*len(ran))
        elif block==5:
            stimList.extend(allScrambled[ran])
            typeList.extend(['scrambled']*len(ran))
    myarray = []
    for i in range(len(stimList)):
        myarray.append({'stim': stimList[i],'type': typeList[i]}) #puts data into an array of dictionaries that the TrialHandler function will accept
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
        routineTimer.add(3.000000)
        #update component parameters for each repeat
        movie=visual.MovieStim(win=win, name='movie',
            filename=stim,
            ori=0, pos=[0, 0], opacity=1,
            depth=0.0,
            )
        #keep track of which components have finished
        trialComponents=[]
        trialComponents.append(movie)
        for thisComponent in trialComponents:
            if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
        #-------Start Routine "trial"-------
        continueRoutine=True
        while continueRoutine and routineTimer.getTime()>0:
            #get current time
            t=trialClock.getTime()
            frameN=frameN+1#number of completed frames (so 0 in first frame)
            #update/draw components on each frame
            
            #*movie* updates
            if t>=0.0 and movie.status==NOT_STARTED:
                #keep track of start time/frame for later
                movie.tStart=t#underestimates by a little under one frame
                movie.frameNStart=frameN#exact frame index
                movie.setAutoDraw(True)
                stimOn=begExpClock.getTime()
            elif movie.status==STARTED and t>=(0.0+3.0):
                movie.setAutoDraw(False)
            
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
        thisExp.nextEntry()
        
        #Add data to output file
        datFile.write('%s\t%s\t%s\t%s\n'%(trials.thisTrialN+1,stim,type,stimOn))
    rep=rep+1
thisExp.nextEntry()

#set up handler to look after randomisation of conditions etc
allColors=np.array(['darkgreen','red','blue','yellow','orange','lime','brown','cyan','purple','violet'])
myarray = []
for i in range(6):
    myarray.append({'color': allColors[i]}) #puts data into an array of dictionaries that the TrialHandler function will accept
fixes=data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=myarray,
    seed=None, name='fixes')
thisExp.addLoop(fixes)#add the loop to the experiment
thisFixe=fixes.trialList[0]#so we can initialise stimuli with some values
#abbreviate parameter names if possible (e.g. rgb=thisFixe.rgb)
if thisFixe!=None:
    for paramName in thisFixe.keys():
        exec(paramName+'=thisFixe.'+paramName)

for thisFixe in fixes:
    currentLoop = fixes
    #abbrieviate parameter names if possible (e.g. rgb=thisFixe.rgb)
    if thisFixe!=None:
        for paramName in thisFixe.keys():
            exec(paramName+'=thisFixe.'+paramName)
    
    #------Prepare to start Routine"fix"-------
    t=0; fixClock.reset() #clock 
    frameN=-1
    routineTimer.add(1.000000)
    #update component parameters for each repeat
    fullscreen.setColor(color, colorSpace=u'rgb')
    #keep track of which components have finished
    fixComponents=[]
    fixComponents.append(fullscreen)
    for thisComponent in fixComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "fix"-------
    continueRoutine=True
    while continueRoutine and routineTimer.getTime()>0:
        #get current time
        t=fixClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*fullscreen* updates
        if t>=0.0 and fullscreen.status==NOT_STARTED:
            #keep track of start time/frame for later
            fullscreen.tStart=t#underestimates by a little under one frame
            fullscreen.frameNStart=frameN#exact frame index
            fullscreen.setAutoDraw(True)
        elif fullscreen.status==STARTED and t>=(0.0+1.0):
            fullscreen.setAutoDraw(False)
        
        #check if all components have finished
        if not continueRoutine: #a component has requested that we end
            routineTimer.reset() #this is the new t0 for non-slip Routines
            break
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #End of Routine "fix"
    for thisComponent in fixComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    thisExp.nextEntry()

#completed 1 repeats of 'fixes'


#Shutting down:
win.close()
core.quit()
