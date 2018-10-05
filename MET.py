#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), Fri Mar 28 16:46:47 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle, seed
import os  # handy system and path functions
import glob

# Store info about the experiment session
expName = u'MET_skeleton'  # from the Builder filename that created this script
expInfo = {'participant':'','group':'pilot', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s_%s' %(expInfo['group'], expInfo['participant'], expInfo['session'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
datFile=open(filename+'.txt','a')
datFile.write('Block\tTrial\tImage\tCondition\tValence\tResponse\tRT\tAccuracy\n')

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace=u'rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instructions1 = visual.TextStim(win=win, ori=0, name='instructions1',
    text=u'In the following test you will see pictures of people in different emotional states. Each picture will be shown twice over the course of the experiment.\r\n\r\nWe would like you to answer the following two questions for each pictures:\r\n\r\n1. What emotion is this person feeling?\r\n\r\n2. How much do you feel what this person is feeling?\r\n',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instructions2 = visual.TextStim(win=win, ori=0, name='instructions2',
    text=u'Here is an example of the first type of question:\r\n\r\nWhat emotion is this person feeling?',    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
instr2_image = visual.PatchStim(win=win, name='instr2_image',units=u'pix', 
    tex=u'instructions_image.jpg', mask=None,
    ori=0, pos=[0, 0], size=[590, 429],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
instr2_choices = visual.TextStim(win=win, ori=0, name='instr2_choices',
    text=u'1. proud    2. joyful    3. happy    4. relieved',    font=u'Arial',
    pos=[0, -0.75], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "instr3"
instr3Clock = core.Clock()
instructions3 = visual.TextStim(win=win, ori=0, name='instructions3',
    text=u"For each picture you will be presented with 4 possible answers. During the task, please press the button that corresponds to the answer that BEST describes the emotion the person is feeling.\r\n\r\nSometimes multiple answers will apply to one image. You must choose which word is the one that best describes the emotion being displayed.\r\n\r\nPress 'return' to continue\r\n",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instr4"
instr4Clock = core.Clock()
instructions4 = visual.TextStim(win=win, ori=0, name='instructions4',
    text=u'Here is an example of the second type of question:\r\n\r\nHow much do you feel what this person is feeling?',    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
instr4_image = visual.PatchStim(win=win, name='instr4_image',units=u'pix', 
    tex=u'instructions_image.jpg', mask=None,
    ori=0, pos=[0, 0], size=[590, 429],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
instr4_choices = visual.TextStim(win=win, ori=0, name='instr4_choices',
    text=u'1       2       3       4       5       6       7       8       9',    font=u'Arial',
    pos=[0, -0.7], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
instr4_explanation = visual.TextStim(win=win, ori=0, name='instr4_explanation',
    text=u'(not at all)                                                        (very much)',    font=u'Arial',
    pos=[0, -0.85], height=0.1, wrapWidth=1.8,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "instr5"
instr5Clock = core.Clock()
instructions5 = visual.TextStim(win=win, ori=0, name='instructions5',
    text=u'During the task, please try to rate how much you feel what the person is feeling (e.g. to what degree you feel sad when looking at a sad person).\r\n\r\nIf you dont feel what the person is feeling at all, press "1". If you strongly feel what the person is feeling, press "9". If your feelings lie between the extremes, you should press the button for one of the increments between 1 and 9.\r\n\r\nPress \'return\' to continue.\r\n',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instr6"
instr6Clock = core.Clock()
instructions6 = visual.TextStim(win=win, ori=0, name='instructions6',
    text=u"During the experiment you will answer the same question for a block of 10 pictures. That question will appear before the block and you will need to hit 'return' to go on. There will be 8 blocks altogether.\r\n\r\nPlease answer the questions as quickly and as accurately as possible.\r\n\r\nThe test will start when you press 'return'\r\n",    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "cog_instr"
cog_instrClock = core.Clock()
cog_instructions = visual.TextStim(win=win, ori=0, name='cog_instructions',
    text=u'What emotion is this person feeling?',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.8,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "cog"
cogClock = core.Clock()
cog_question = visual.TextStim(win=win, ori=0, name='cog_question',
    text=u'What emotion is this person feeling?',    font=u'Arial',
    pos=[0, 0.75], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
cog_image = visual.PatchStim(win=win, name='cog_image',units=u'pix', 
    tex='sin', mask=None,
    ori=0, pos=[0, 0], size=[602, 352],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
cog_choices = visual.TextStim(win=win, ori=0, name='cog_choices',
    text='nonsense',    font=u'Arial',
    pos=[0, -0.75], height=0.1, wrapWidth=1.8,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "emo_instr"
emo_instrClock = core.Clock()
emo_instructions = visual.TextStim(win=win, ori=0, name='emo_instructions',
    text=u'How much do you feel what this person is feeling?',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.8,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "emo"
emoClock = core.Clock()
emo_question = visual.TextStim(win=win, ori=0, name='emo_question',
    text=u'How much do you feel what this person is feeling?',    font=u'Arial',
    pos=[0, 0.75], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
emo_image = visual.PatchStim(win=win, name='emo_image',units=u'pix', 
    tex='sin', mask=None,
    ori=0, pos=[0, 0], size=[602, 352],
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
emo_choices = visual.TextStim(win=win, ori=0, name='emo_choices',
    text=u'1       2       3       4       5       6       7       8       9',    font=u'Arial',
    pos=[0, -0.7], height=0.1, wrapWidth=1.5,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
emo_explanation = visual.TextStim(win=win, ori=0, name='emo_explanation',
    text=u'(not at all)                                                        (very much)',    font=u'Arial',
    pos=[0, -0.85], height=0.1, wrapWidth=1.8,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-4.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_instr1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_instr1.status = NOT_STARTED
# keep track of which components have finished
instr1Components = []
instr1Components.append(instructions1)
instr1Components.append(key_resp_instr1)
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions1* updates
    if t >= 0.0 and instructions1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions1.tStart = t  # underestimates by a little under one frame
        instructions1.frameNStart = frameN  # exact frame index
        instructions1.setAutoDraw(True)
    
    # *key_resp_instr1* updates
    if t >= 0.0 and key_resp_instr1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instr1.tStart = t  # underestimates by a little under one frame
        key_resp_instr1.frameNStart = frameN  # exact frame index
        key_resp_instr1.status = STARTED
        # keyboard checking is just starting
        key_resp_instr1.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_instr1.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_instr1.keys = theseKeys[-1]  # just the last key pressed
            key_resp_instr1.rt = key_resp_instr1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instr2"-------
t = 0
instr2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_instr2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_instr2.status = NOT_STARTED
# keep track of which components have finished
instr2Components = []
instr2Components.append(instructions2)
instr2Components.append(instr2_image)
instr2Components.append(instr2_choices)
instr2Components.append(key_resp_instr2)
for thisComponent in instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions2* updates
    if t >= 0.0 and instructions2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions2.tStart = t  # underestimates by a little under one frame
        instructions2.frameNStart = frameN  # exact frame index
        instructions2.setAutoDraw(True)
    
    # *instr2_image* updates
    if t >= 0.0 and instr2_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2_image.tStart = t  # underestimates by a little under one frame
        instr2_image.frameNStart = frameN  # exact frame index
        instr2_image.setAutoDraw(True)
    
    # *instr2_choices* updates
    if t >= 0.0 and instr2_choices.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr2_choices.tStart = t  # underestimates by a little under one frame
        instr2_choices.frameNStart = frameN  # exact frame index
        instr2_choices.setAutoDraw(True)
    
    # *key_resp_instr2* updates
    if t >= 0.0 and key_resp_instr2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instr2.tStart = t  # underestimates by a little under one frame
        key_resp_instr2.frameNStart = frameN  # exact frame index
        key_resp_instr2.status = STARTED
        # keyboard checking is just starting
        key_resp_instr2.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_instr2.status == STARTED:
        theseKeys = event.getKeys(keyList=['return', '1', '2', '3', '4'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_instr2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_instr2.rt = key_resp_instr2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instr2"-------
for thisComponent in instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instr3"-------
t = 0
instr3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_instr3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_instr3.status = NOT_STARTED
# keep track of which components have finished
instr3Components = []
instr3Components.append(instructions3)
instr3Components.append(key_resp_instr3)
for thisComponent in instr3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions3* updates
    if t >= 0.0 and instructions3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions3.tStart = t  # underestimates by a little under one frame
        instructions3.frameNStart = frameN  # exact frame index
        instructions3.setAutoDraw(True)
    
    # *key_resp_instr3* updates
    if t >= 0.0 and key_resp_instr3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instr3.tStart = t  # underestimates by a little under one frame
        key_resp_instr3.frameNStart = frameN  # exact frame index
        key_resp_instr3.status = STARTED
        # keyboard checking is just starting
        key_resp_instr3.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_instr3.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_instr3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_instr3.rt = key_resp_instr3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instr3"-------
for thisComponent in instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instr4"-------
t = 0
instr4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_instr4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_instr4.status = NOT_STARTED
# keep track of which components have finished
instr4Components = []
instr4Components.append(instructions4)
instr4Components.append(instr4_image)
instr4Components.append(instr4_choices)
instr4Components.append(instr4_explanation)
instr4Components.append(key_resp_instr4)
for thisComponent in instr4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions4* updates
    if t >= 0.0 and instructions4.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions4.tStart = t  # underestimates by a little under one frame
        instructions4.frameNStart = frameN  # exact frame index
        instructions4.setAutoDraw(True)
    
    # *instr4_image* updates
    if t >= 0.0 and instr4_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr4_image.tStart = t  # underestimates by a little under one frame
        instr4_image.frameNStart = frameN  # exact frame index
        instr4_image.setAutoDraw(True)
    
    # *instr4_choices* updates
    if t >= 0.0 and instr4_choices.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr4_choices.tStart = t  # underestimates by a little under one frame
        instr4_choices.frameNStart = frameN  # exact frame index
        instr4_choices.setAutoDraw(True)
    
    # *instr4_explanation* updates
    if t >= 0.0 and instr4_explanation.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr4_explanation.tStart = t  # underestimates by a little under one frame
        instr4_explanation.frameNStart = frameN  # exact frame index
        instr4_explanation.setAutoDraw(True)
    
    # *key_resp_instr4* updates
    if t >= 0.0 and key_resp_instr4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instr4.tStart = t  # underestimates by a little under one frame
        key_resp_instr4.frameNStart = frameN  # exact frame index
        key_resp_instr4.status = STARTED
        # keyboard checking is just starting
        key_resp_instr4.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_instr4.status == STARTED:
        theseKeys = event.getKeys(keyList=['return', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_instr4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_instr4.rt = key_resp_instr4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instr4"-------
for thisComponent in instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instr5"-------
t = 0
instr5Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_instr5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_instr5.status = NOT_STARTED
# keep track of which components have finished
instr5Components = []
instr5Components.append(instructions5)
instr5Components.append(key_resp_instr5)
for thisComponent in instr5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr5"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions5* updates
    if t >= 0.0 and instructions5.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions5.tStart = t  # underestimates by a little under one frame
        instructions5.frameNStart = frameN  # exact frame index
        instructions5.setAutoDraw(True)
    
    # *key_resp_instr5* updates
    if t >= 0.0 and key_resp_instr5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instr5.tStart = t  # underestimates by a little under one frame
        key_resp_instr5.frameNStart = frameN  # exact frame index
        key_resp_instr5.status = STARTED
        # keyboard checking is just starting
        key_resp_instr5.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_instr5.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_instr5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_instr5.rt = key_resp_instr5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instr5"-------
for thisComponent in instr5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instr6"-------
t = 0
instr6Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_instr6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_instr6.status = NOT_STARTED
# keep track of which components have finished
instr6Components = []
instr6Components.append(instructions6)
instr6Components.append(key_resp_instr6)
for thisComponent in instr6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr6"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions6* updates
    if t >= 0.0 and instructions6.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions6.tStart = t  # underestimates by a little under one frame
        instructions6.frameNStart = frameN  # exact frame index
        instructions6.setAutoDraw(True)
    
    # *key_resp_instr6* updates
    if t >= 0.0 and key_resp_instr6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instr6.tStart = t  # underestimates by a little under one frame
        key_resp_instr6.frameNStart = frameN  # exact frame index
        key_resp_instr6.status = STARTED
        # keyboard checking is just starting
        key_resp_instr6.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_instr6.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_instr6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_instr6.rt = key_resp_instr6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instr6"-------
for thisComponent in instr6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=8, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

#counterbalance = randint(1,9)
counterbalance=4
cog_data=np.genfromtxt('conditions.txt',dtype=str,skip_header=1)
shuffle(cog_data)
cog_sorted=cog_data[np.argsort(cog_data[:,7])]
cog_schedule = range(4)
shuffle(cog_schedule)

emo_data=np.genfromtxt('conditions.txt',dtype=str,skip_header=1)
shuffle(emo_data)
emo_sorted=emo_data[np.argsort(emo_data[:,7])]
emo_schedule = range(4)
shuffle(emo_schedule)

cog_loop=0
emo_loop=0
for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    if counterbalance % 2 == 0:
        #------Prepare to start Routine "cog_instr"-------
        t = 0
        cog_instrClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        key_resp_cog_instr = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_cog_instr.status = NOT_STARTED
        # keep track of which components have finished
        cog_instrComponents = []
        cog_instrComponents.append(cog_instructions)
        cog_instrComponents.append(key_resp_cog_instr)
        for thisComponent in cog_instrComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "cog_instr"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = cog_instrClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cog_instructions* updates
            if t >= 0.0 and cog_instructions.status == NOT_STARTED:
                # keep track of start time/frame for later
                cog_instructions.tStart = t  # underestimates by a little under one frame
                cog_instructions.frameNStart = frameN  # exact frame index
                cog_instructions.setAutoDraw(True)
            
            # *key_resp_cog_instr* updates
            if t >= 0.0 and key_resp_cog_instr.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_cog_instr.tStart = t  # underestimates by a little under one frame
                key_resp_cog_instr.frameNStart = frameN  # exact frame index
                key_resp_cog_instr.status = STARTED
                # keyboard checking is just starting
                key_resp_cog_instr.clock.reset()  # now t=0
                event.clearEvents()
            if key_resp_cog_instr.status == STARTED:
                theseKeys = event.getKeys(keyList=['return'])
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_cog_instr.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_cog_instr.rt = key_resp_cog_instr.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cog_instrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "cog_instr"-------
        for thisComponent in cog_instrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_cog_instr.keys in ['', [], None]:  # No response was made
           key_resp_cog_instr.keys=None
        # store data for blocks (TrialHandler)
        blocks.addData('key_resp_cog_instr.keys',key_resp_cog_instr.keys)
        if key_resp_cog_instr.keys != None:  # we had a response
            blocks.addData('key_resp_cog_instr.rt', key_resp_cog_instr.rt)
        
        # set up handler to look after randomisation of conditions etc
        cog_thisloop=cog_sorted[cog_schedule[cog_loop]*10:(cog_schedule[cog_loop]*10)+10]
        myarray=[]
        for i in range(len(cog_thisloop)):
            myarray.append({'stim1': cog_thisloop[i,0], 'choice1': cog_thisloop[i,1], 'choice2': cog_thisloop[i,2], 'choice3': cog_thisloop[i,3], 'choice4': cog_thisloop[i,4], 'corr': cog_thisloop[i,5], 'val': cog_thisloop[i,7]}) #puts data into an array of dictionaries that the TrialHandler function will accept
        cogs = data.TrialHandler(nReps=1, method=u'sequential', 
            extraInfo=expInfo, originPath=None,
            trialList=myarray,
            seed=None, name='cogs')
        thisExp.addLoop(cogs)  # add the loop to the experiment
        thisCog = cogs.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisCog.rgb)
        if thisCog != None:
            for paramName in thisCog.keys():
                exec(paramName + '= thisCog.' + paramName)
        
        for thisCog in cogs:
            currentLoop = cogs
            # abbreviate parameter names if possible (e.g. rgb = thisCog.rgb)
            if thisCog != None:
                for paramName in thisCog.keys():
                    exec(paramName + '= thisCog.' + paramName)
            
            #------Prepare to start Routine "cog"-------
            t = 0
            cogClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            cog_image.setImage(stim1)
            cog_choices.setText(u'1. %s    2. %s    3. %s    4. %s'%(choice1,choice2,choice3,choice4))
            key_resp_cog = event.BuilderKeyResponse()  # create an object of type KeyResponse
            key_resp_cog.status = NOT_STARTED
            # keep track of which components have finished
            cogComponents = []
            cogComponents.append(cog_question)
            cogComponents.append(cog_image)
            cogComponents.append(cog_choices)
            cogComponents.append(key_resp_cog)
            for thisComponent in cogComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "cog"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = cogClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cog_question* updates
                if t >= 0.0 and cog_question.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    cog_question.tStart = t  # underestimates by a little under one frame
                    cog_question.frameNStart = frameN  # exact frame index
                    cog_question.setAutoDraw(True)
                
                # *cog_image* updates
                if t >= 0.0 and cog_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    cog_image.tStart = t  # underestimates by a little under one frame
                    cog_image.frameNStart = frameN  # exact frame index
                    cog_image.setAutoDraw(True)
                
                # *cog_choices* updates
                if t >= 0.0 and cog_choices.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    cog_choices.tStart = t  # underestimates by a little under one frame
                    cog_choices.frameNStart = frameN  # exact frame index
                    cog_choices.setAutoDraw(True)
                
                # *key_resp_cog* updates
                if t >= 0.0 and key_resp_cog.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_cog.tStart = t  # underestimates by a little under one frame
                    key_resp_cog.frameNStart = frameN  # exact frame index
                    key_resp_cog.status = STARTED
                    # keyboard checking is just starting
                    key_resp_cog.clock.reset()  # now t=0
                    event.clearEvents()
                if key_resp_cog.status == STARTED:
                    theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_cog.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_cog.rt = key_resp_cog.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cogComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
                else:  # this Routine was not non-slip safe so reset non-slip timer
                    routineTimer.reset()
            
            #-------Ending Routine "cog"-------
            for thisComponent in cogComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_cog.keys in ['', [], None]:  # No response was made
               key_resp_cog.keys=None
            # store data for cogs (TrialHandler)
            cogs.addData('key_resp_cog.keys',key_resp_cog.keys)
            if key_resp_cog.keys != None:  # we had a response
                cogs.addData('key_resp_cog.rt', key_resp_cog.rt)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'cogs'
            if key_resp_cog.keys==corr:
                acc=1
            else:
                acc=0
            datFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(blocks.thisN+1,cogs.thisN+1,stim1,'cog',val,key_resp_cog.keys,key_resp_cog.rt,acc))
        cog_loop = cog_loop + 1
    elif counterbalance % 2 != 0:
        #------Prepare to start Routine "emo_instr"-------
        t = 0
        emo_instrClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        key_resp_emo_instr = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_emo_instr.status = NOT_STARTED
        # keep track of which components have finished
        emo_instrComponents = []
        emo_instrComponents.append(emo_instructions)
        emo_instrComponents.append(key_resp_emo_instr)
        for thisComponent in emo_instrComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "emo_instr"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = emo_instrClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *emo_instructions* updates
            if t >= 0.0 and emo_instructions.status == NOT_STARTED:
                # keep track of start time/frame for later
                emo_instructions.tStart = t  # underestimates by a little under one frame
                emo_instructions.frameNStart = frameN  # exact frame index
                emo_instructions.setAutoDraw(True)
            
            # *key_resp_emo_instr* updates
            if t >= 0.0 and key_resp_emo_instr.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_emo_instr.tStart = t  # underestimates by a little under one frame
                key_resp_emo_instr.frameNStart = frameN  # exact frame index
                key_resp_emo_instr.status = STARTED
                # keyboard checking is just starting
                key_resp_emo_instr.clock.reset()  # now t=0
                event.clearEvents()
            if key_resp_emo_instr.status == STARTED:
                theseKeys = event.getKeys(keyList=['return'])
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_emo_instr.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_emo_instr.rt = key_resp_emo_instr.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in emo_instrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "emo_instr"-------
        for thisComponent in emo_instrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_emo_instr.keys in ['', [], None]:  # No response was made
           key_resp_emo_instr.keys=None
        # store data for blocks (TrialHandler)
        blocks.addData('key_resp_emo_instr.keys',key_resp_emo_instr.keys)
        if key_resp_emo_instr.keys != None:  # we had a response
            blocks.addData('key_resp_emo_instr.rt', key_resp_emo_instr.rt)
        
        # set up handler to look after randomisation of conditions etc
        emo_thisloop=emo_sorted[emo_schedule[emo_loop]*10:(emo_schedule[emo_loop]*10)+10]
        myarray2=[]
        for i in range(len(emo_thisloop)):
            myarray2.append({'stim2': emo_thisloop[i,0], 'val': emo_thisloop[i,7]})
        emos = data.TrialHandler(nReps=1, method=u'sequential', 
            extraInfo=expInfo, originPath=None,
            trialList=myarray2,
            seed=None, name='emos')
        thisExp.addLoop(emos)  # add the loop to the experiment
        thisEmo = emos.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisEmo.rgb)
        if thisEmo != None:
            for paramName in thisEmo.keys():
                exec(paramName + '= thisEmo.' + paramName)
        
        for thisEmo in emos:
            currentLoop = emos
            # abbreviate parameter names if possible (e.g. rgb = thisEmo.rgb)
            if thisEmo != None:
                for paramName in thisEmo.keys():
                    exec(paramName + '= thisEmo.' + paramName)
            
            #------Prepare to start Routine "emo"-------
            t = 0
            emoClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            emo_image.setImage(stim2)
            key_resp_emo = event.BuilderKeyResponse()  # create an object of type KeyResponse
            key_resp_emo.status = NOT_STARTED
            # keep track of which components have finished
            emoComponents = []
            emoComponents.append(emo_question)
            emoComponents.append(emo_image)
            emoComponents.append(emo_choices)
            emoComponents.append(key_resp_emo)
            emoComponents.append(emo_explanation)
            for thisComponent in emoComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "emo"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = emoClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *emo_question* updates
                if t >= 0.0 and emo_question.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    emo_question.tStart = t  # underestimates by a little under one frame
                    emo_question.frameNStart = frameN  # exact frame index
                    emo_question.setAutoDraw(True)
                
                # *emo_image* updates
                if t >= 0.0 and emo_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    emo_image.tStart = t  # underestimates by a little under one frame
                    emo_image.frameNStart = frameN  # exact frame index
                    emo_image.setAutoDraw(True)
                
                # *emo_choices* updates
                if t >= 0.0 and emo_choices.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    emo_choices.tStart = t  # underestimates by a little under one frame
                    emo_choices.frameNStart = frameN  # exact frame index
                    emo_choices.setAutoDraw(True)
                
                # *key_resp_emo* updates
                if t >= 0.0 and key_resp_emo.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_emo.tStart = t  # underestimates by a little under one frame
                    key_resp_emo.frameNStart = frameN  # exact frame index
                    key_resp_emo.status = STARTED
                    # keyboard checking is just starting
                    key_resp_emo.clock.reset()  # now t=0
                    event.clearEvents()
                if key_resp_emo.status == STARTED:
                    theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_emo.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_emo.rt = key_resp_emo.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # *emo_explanation* updates
                if t >= 0.0 and emo_explanation.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    emo_explanation.tStart = t  # underestimates by a little under one frame
                    emo_explanation.frameNStart = frameN  # exact frame index
                    emo_explanation.setAutoDraw(True)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in emoComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
                else:  # this Routine was not non-slip safe so reset non-slip timer
                    routineTimer.reset()
            
            #-------Ending Routine "emo"-------
            for thisComponent in emoComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_emo.keys in ['', [], None]:  # No response was made
               key_resp_emo.keys=None
            # store data for emos (TrialHandler)
            emos.addData('key_resp_emo.keys',key_resp_emo.keys)
            if key_resp_emo.keys != None:  # we had a response
                emos.addData('key_resp_emo.rt', key_resp_emo.rt)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'emos'
            datFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(blocks.thisN+1,emos.thisN+1,stim2,'emo',val,key_resp_emo.keys,key_resp_emo.rt,'N/A'))
        emo_loop = emo_loop + 1
        
        thisExp.nextEntry()
    counterbalance = counterbalance + 1
# completed 4 repeats of 'blocks'

win.close()
core.quit()
