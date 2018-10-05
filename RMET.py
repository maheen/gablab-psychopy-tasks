#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), Fri Jan 17 14:46:44 2014
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
import os #handy system and path functions

#store info about the experiment session
expName='RMET_skeleton'#from the Builder filename that created this script
expInfo={'participant':'','group':'pilot', 'session':'001'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
filename='data' + os.path.sep + '%s_%s_%s' %(expInfo['group'], expInfo['participant'], expInfo['session'])
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#an ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
datFile=open(filename+'.txt','a')
datFile.write('Trial\tpicID\tanswer\thit\tRT\n')

#setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'white', colorSpace=u'rgb')

#Initialise components for Routine "instr"
instrClock=core.Clock()
instructions=visual.TextStim(win=win, ori=0, name='instructions',
    text="For each set of eyes, select the number corresponding to the word that best describes what the person in the picture is thinking or feeling. You may feel that more than one word is applicable, but please choose just one word, the word which you consider to be most suitable. Before making your choice, make sure that you have read all 4 words. You should try to do the task as quickly as possible but you will not be timed.  Press 'enter' to begin.",
    font='Arial',
    pos=[0, 0], height=0.05,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

#Initialise components for Routine "pract"
practClock=core.Clock()
practice=visual.PatchStim(win=win, name='practice',
    tex='stimuli/pic00.jpg', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
pract_w1=visual.TextStim(win=win, ori=0, name='pract_w1',
    text='jealous',
    font='Arial',
    pos=[-0.5, 0.5], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
pract_w2=visual.TextStim(win=win, ori=0, name='pract_w2',
    text='panicked',
    font='Arial',
    pos=[0.5, 0.5], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
pract_w3=visual.TextStim(win=win, ori=0, name='pract_w3',
    text='arrogant',
    font='Arial',
    pos=[-0.5, -0.5], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
pract_w4=visual.TextStim(win=win, ori=0, name='pract_w4',
    text='hateful',
    font='Arial',
    pos=[0.5, -0.5], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

#Initialise components for Routine "trial"
trialClock=core.Clock()
stimulus=visual.PatchStim(win=win, name='stimulus',
    tex='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
trial_word1=visual.TextStim(win=win, ori=0, name='trial_word1',
    text='nonsense',
    font=u'Arial',
    pos=[-0.5, 0.5], height=0.1,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-1.0)
trial_word2=visual.TextStim(win=win, ori=0, name='trial_word2',
    text='nonsense',
    font=u'Arial',
    pos=[0.5, 0.5], height=0.1,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
trial_word3=visual.TextStim(win=win, ori=0, name='trial_word3',
    text='nonsense',
    font=u'Arial',
    pos=[-0.5, -0.5], height=0.1,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-3.0)
trial_word4=visual.TextStim(win=win, ori=0, name='trial_word4',
    text='nonsense',
    font=u'Arial',
    pos=[0.5, -0.5], height=0.1,wrapWidth=None,
    color=u'black', colorSpace=u'rgb', opacity=1,
    depth=-4.0)

# Create some handy timers
globalClock=core.Clock() #to track the time since experiment started
routineTimer=core.CountdownTimer() #to track time remaining of each (non-slip) routine 

#------Prepare to start Routine"instr"-------
t=0; instrClock.reset() #clock 
frameN=-1
#update component parameters for each repeat
instr_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
instr_resp.status=NOT_STARTED
#keep track of which components have finished
instrComponents=[]
instrComponents.append(instructions)
instrComponents.append(instr_resp)
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
    
    #*instr_resp* updates
    if t>=0.0 and instr_resp.status==NOT_STARTED:
        #keep track of start time/frame for later
        instr_resp.tStart=t#underestimates by a little under one frame
        instr_resp.frameNStart=frameN#exact frame index
        instr_resp.status=STARTED
        #keyboard checking is just starting
        instr_resp.clock.reset() # now t=0
        event.clearEvents()
    if instr_resp.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys)>0:#at least one key was pressed
            instr_resp.keys=theseKeys[-1]#just the last key pressed
            instr_resp.rt = instr_resp.clock.getTime()
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

#------Prepare to start Routine"pract"-------
t=0; practClock.reset() #clock 
frameN=-1
#update component parameters for each repeat
pract_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
pract_resp.status=NOT_STARTED
#keep track of which components have finished
practComponents=[]
practComponents.append(practice)
practComponents.append(pract_w1)
practComponents.append(pract_w2)
practComponents.append(pract_w3)
practComponents.append(pract_w4)
practComponents.append(pract_resp)
for thisComponent in practComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#-------Start Routine "pract"-------
continueRoutine=True
while continueRoutine:
    #get current time
    t=practClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*practice* updates
    if t>=0.0 and practice.status==NOT_STARTED:
        #keep track of start time/frame for later
        practice.tStart=t#underestimates by a little under one frame
        practice.frameNStart=frameN#exact frame index
        practice.setAutoDraw(True)
    
    #*pract_w1* updates
    if t>=0.0 and pract_w1.status==NOT_STARTED:
        #keep track of start time/frame for later
        pract_w1.tStart=t#underestimates by a little under one frame
        pract_w1.frameNStart=frameN#exact frame index
        pract_w1.setAutoDraw(True)
    
    #*pract_w2* updates
    if t>=0.0 and pract_w2.status==NOT_STARTED:
        #keep track of start time/frame for later
        pract_w2.tStart=t#underestimates by a little under one frame
        pract_w2.frameNStart=frameN#exact frame index
        pract_w2.setAutoDraw(True)
    
    #*pract_w3* updates
    if t>=0.0 and pract_w3.status==NOT_STARTED:
        #keep track of start time/frame for later
        pract_w3.tStart=t#underestimates by a little under one frame
        pract_w3.frameNStart=frameN#exact frame index
        pract_w3.setAutoDraw(True)
    
    #*pract_w4* updates
    if t>=0.0 and pract_w4.status==NOT_STARTED:
        #keep track of start time/frame for later
        pract_w4.tStart=t#underestimates by a little under one frame
        pract_w4.frameNStart=frameN#exact frame index
        pract_w4.setAutoDraw(True)
    
    #*pract_resp* updates
    if t>=0.0 and pract_resp.status==NOT_STARTED:
        #keep track of start time/frame for later
        pract_resp.tStart=t#underestimates by a little under one frame
        pract_resp.frameNStart=frameN#exact frame index
        pract_resp.status=STARTED
        #keyboard checking is just starting
        pract_resp.clock.reset() # now t=0
        event.clearEvents()
    if pract_resp.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
        if len(theseKeys)>0:#at least one key was pressed
            pract_resp.keys=theseKeys[-1]#just the last key pressed
            pract_resp.rt = pract_resp.clock.getTime()
            #was this 'correct'?
            if (pract_resp.keys==str("'2'")): pract_resp.corr=1
            else: pract_resp.corr=0
            #abort routine on response
            continueRoutine=False
    
    #check if all components have finished
    if not continueRoutine: #a component has requested that we end
        routineTimer.reset() #this is the new t0 for non-slip Routines
        break
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in practComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#End of Routine "pract"
for thisComponent in practComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)

#set up handler to look after randomisation of conditions etc
trials=data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('conditions.xlsx'),
    seed=int(expInfo['participant']), name='trials')
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
    stimulus.setImage(stim)
    trial_word1.setText(word1)
    trial_word2.setText(word2)
    trial_word3.setText(word3)
    trial_word4.setText(word4)
    key_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    key_resp.status=NOT_STARTED
    #keep track of which components have finished
    trialComponents=[]
    trialComponents.append(stimulus)
    trialComponents.append(trial_word1)
    trialComponents.append(trial_word2)
    trialComponents.append(trial_word3)
    trialComponents.append(trial_word4)
    trialComponents.append(key_resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "trial"-------
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*stimulus* updates
        if t>=0.0 and stimulus.status==NOT_STARTED:
            #keep track of start time/frame for later
            stimulus.tStart=t#underestimates by a little under one frame
            stimulus.frameNStart=frameN#exact frame index
            stimulus.setAutoDraw(True)
        
        #*trial_word1* updates
        if t>=0.0 and trial_word1.status==NOT_STARTED:
            #keep track of start time/frame for later
            trial_word1.tStart=t#underestimates by a little under one frame
            trial_word1.frameNStart=frameN#exact frame index
            trial_word1.setAutoDraw(True)
        
        #*trial_word2* updates
        if t>=0.0 and trial_word2.status==NOT_STARTED:
            #keep track of start time/frame for later
            trial_word2.tStart=t#underestimates by a little under one frame
            trial_word2.frameNStart=frameN#exact frame index
            trial_word2.setAutoDraw(True)
        
        #*trial_word3* updates
        if t>=0.0 and trial_word3.status==NOT_STARTED:
            #keep track of start time/frame for later
            trial_word3.tStart=t#underestimates by a little under one frame
            trial_word3.frameNStart=frameN#exact frame index
            trial_word3.setAutoDraw(True)
        
        #*trial_word4* updates
        if t>=0.0 and trial_word4.status==NOT_STARTED:
            #keep track of start time/frame for later
            trial_word4.tStart=t#underestimates by a little under one frame
            trial_word4.frameNStart=frameN#exact frame index
            trial_word4.setAutoDraw(True)
        
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
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            if len(theseKeys)>0:#at least one key was pressed
                key_resp.keys=theseKeys[-1]#just the last key pressed
                key_resp.rt = key_resp.clock.getTime()
                #was this 'correct'?
                if (key_resp.keys==str(correctResponse)): key_resp.corr=1
                else: key_resp.corr=0
                #abort routine on response
                continueRoutine=False
        
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
       #was no response the correct answer?!
       if str(correctResponse).lower()=='none':key_resp.corr=1 #correct non-response
       else: key_resp.corr=0 #failed to respond (incorrectly)
    #store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr',key_resp.corr)
    if key_resp.keys != None:#we had a response
        trials.addData('key_resp.rt',key_resp.rt)
    thisExp.nextEntry()

#completed 1 repeats of 'trials'
    datFile.write('%s\t%s\t%s\t%s\t%s\n'%(trials.thisTrialN+1,stim[11:13],key_resp.keys,key_resp.corr,key_resp.rt))

#save data for this loop
#trials.saveAsPickle(filename+'trials', fileCollisionMethod='rename')

#Shutting down:
win.close()
core.quit()
