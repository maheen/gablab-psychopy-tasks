#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), Tue May 20 14:28:22 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'MASC_skeleton'  # from the Builder filename that created this script
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
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instructions1 = visual.TextStim(win=win, ori=0, name='instructions1',
    text='You will be watching a 15 minute film. Please watch very carefully and try to understand what each character is feeling or thinking.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.3,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instructions2 = visual.TextStim(win=win, ori=0, name='instructions2',
    text='Now, you will meet each character.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "char1"
char1Clock = core.Clock()
character1 = visual.TextStim(win=win, ori=0, name='character1',
    text='This is Sandra',    font='Arial',
    pos=[0, 0.7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image_char1 = visual.PatchStim(win=win, name='image_char1',units='pix', 
    tex='pictures/sandra.png', mask=None,
    ori=0, pos=[0, -30], size=[580, 450],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "char2"
char2Clock = core.Clock()
character2 = visual.TextStim(win=win, ori=0, name='character2',
    text='This is Michael',    font='Arial',
    pos=[0, 0.7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image_char2 = visual.PatchStim(win=win, name='image_char2',units='pix', 
    tex='pictures/michael.png', mask=None,
    ori=0, pos=[0, -30], size=[580, 450],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "char3"
char3Clock = core.Clock()
character3 = visual.TextStim(win=win, ori=0, name='character3',
    text='This is Betty',    font='Arial',
    pos=[0, 0.7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image_char3 = visual.PatchStim(win=win, name='image_char3',units='pix', 
    tex='pictures/betty.png', mask=None,
    ori=0, pos=[0, -30], size=[580, 450],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "char4"
char4Clock = core.Clock()
character4 = visual.TextStim(win=win, ori=0, name='character4',
    text='This is Cliff',    font='Arial',
    pos=[0, 0.7], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image_char4 = visual.PatchStim(win=win, name='image_char4',units='pix', 
    tex='pictures/cliff.png', mask=None,
    ori=0, pos=[0, -30], size=[580, 450],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instr3"
instr3Clock = core.Clock()
instructions3 = visual.TextStim(win=win, ori=0, name='instructions3',
    text='The file shows these four people getting together for a Saturday evening.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.3,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instr4"
instr4Clock = core.Clock()
instructions4 = visual.TextStim(win=win, ori=0, name='instructions4',
    text='The movie will be stopped at various points and some questions will be asked. All of the answers are multiple choice and require one option to be selected from a choice of four. If you are not exactly sure of the correct answer, please guess.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.3,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instr5"
instr5Clock = core.Clock()
instructions5 = visual.TextStim(win=win, ori=0, name='instructions5',
    text='When you answer, try to imagine what the characters are feeling or thinking at the very moment the film is stopped.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.3,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "instr6"
instr6Clock = core.Clock()
instructions6 = visual.TextStim(win=win, ori=0, name='instructions6',
    text='The first scene is about to start.\r\n\r\nAre you ready?\r\n\r\nAgain, please watch very carefully because each scene will be presented only once.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.3,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "vid"
vidClock = core.Clock()

# Initialize components for Routine "quest"
questClock = core.Clock()
image = visual.PatchStim(win=win, name='image',units='pix', 
    tex='sin', mask=None,
    ori=0, pos=[0, 0], size=[1280, 800],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, ori=0, name='thanks',
    text='Thank you for your participation!',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

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
        theseKeys = event.getKeys(keyList=['return'])
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

#------Prepare to start Routine "char1"-------
t = 0
char1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_char1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_char1.status = NOT_STARTED
# keep track of which components have finished
char1Components = []
char1Components.append(character1)
char1Components.append(key_resp_char1)
char1Components.append(image_char1)
for thisComponent in char1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "char1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = char1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *character1* updates
    if t >= 0.0 and character1.status == NOT_STARTED:
        # keep track of start time/frame for later
        character1.tStart = t  # underestimates by a little under one frame
        character1.frameNStart = frameN  # exact frame index
        character1.setAutoDraw(True)
    
    # *key_resp_char1* updates
    if t >= 0.0 and key_resp_char1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_char1.tStart = t  # underestimates by a little under one frame
        key_resp_char1.frameNStart = frameN  # exact frame index
        key_resp_char1.status = STARTED
        # keyboard checking is just starting
        key_resp_char1.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_char1.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_char1.keys = theseKeys[-1]  # just the last key pressed
            key_resp_char1.rt = key_resp_char1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_char1* updates
    if t >= 0.0 and image_char1.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_char1.tStart = t  # underestimates by a little under one frame
        image_char1.frameNStart = frameN  # exact frame index
        image_char1.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in char1Components:
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

#-------Ending Routine "char1"-------
for thisComponent in char1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "char2"-------
t = 0
char2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_char2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_char2.status = NOT_STARTED
# keep track of which components have finished
char2Components = []
char2Components.append(character2)
char2Components.append(key_resp_char2)
char2Components.append(image_char2)
for thisComponent in char2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "char2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = char2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *character2* updates
    if t >= 0.0 and character2.status == NOT_STARTED:
        # keep track of start time/frame for later
        character2.tStart = t  # underestimates by a little under one frame
        character2.frameNStart = frameN  # exact frame index
        character2.setAutoDraw(True)
    
    # *key_resp_char2* updates
    if t >= 0.0 and key_resp_char2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_char2.tStart = t  # underestimates by a little under one frame
        key_resp_char2.frameNStart = frameN  # exact frame index
        key_resp_char2.status = STARTED
        # keyboard checking is just starting
        key_resp_char2.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_char2.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_char2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_char2.rt = key_resp_char2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_char2* updates
    if t >= 0.0 and image_char2.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_char2.tStart = t  # underestimates by a little under one frame
        image_char2.frameNStart = frameN  # exact frame index
        image_char2.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in char2Components:
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

#-------Ending Routine "char2"-------
for thisComponent in char2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "char3"-------
t = 0
char3Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_char3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_char3.status = NOT_STARTED
# keep track of which components have finished
char3Components = []
char3Components.append(character3)
char3Components.append(key_resp_char3)
char3Components.append(image_char3)
for thisComponent in char3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "char3"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = char3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *character3* updates
    if t >= 0.0 and character3.status == NOT_STARTED:
        # keep track of start time/frame for later
        character3.tStart = t  # underestimates by a little under one frame
        character3.frameNStart = frameN  # exact frame index
        character3.setAutoDraw(True)
    
    # *key_resp_char3* updates
    if t >= 0.0 and key_resp_char3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_char3.tStart = t  # underestimates by a little under one frame
        key_resp_char3.frameNStart = frameN  # exact frame index
        key_resp_char3.status = STARTED
        # keyboard checking is just starting
        key_resp_char3.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_char3.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_char3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_char3.rt = key_resp_char3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_char3* updates
    if t >= 0.0 and image_char3.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_char3.tStart = t  # underestimates by a little under one frame
        image_char3.frameNStart = frameN  # exact frame index
        image_char3.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in char3Components:
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

#-------Ending Routine "char3"-------
for thisComponent in char3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "char4"-------
t = 0
char4Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_char4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_char4.status = NOT_STARTED
# keep track of which components have finished
char4Components = []
char4Components.append(character4)
char4Components.append(key_resp_char4)
char4Components.append(image_char4)
for thisComponent in char4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "char4"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = char4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *character4* updates
    if t >= 0.0 and character4.status == NOT_STARTED:
        # keep track of start time/frame for later
        character4.tStart = t  # underestimates by a little under one frame
        character4.frameNStart = frameN  # exact frame index
        character4.setAutoDraw(True)
    
    # *key_resp_char4* updates
    if t >= 0.0 and key_resp_char4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_char4.tStart = t  # underestimates by a little under one frame
        key_resp_char4.frameNStart = frameN  # exact frame index
        key_resp_char4.status = STARTED
        # keyboard checking is just starting
        key_resp_char4.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_char4.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_char4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_char4.rt = key_resp_char4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_char4* updates
    if t >= 0.0 and image_char4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_char4.tStart = t  # underestimates by a little under one frame
        image_char4.frameNStart = frameN  # exact frame index
        image_char4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in char4Components:
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

#-------Ending Routine "char4"-------
for thisComponent in char4Components:
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
        theseKeys = event.getKeys(keyList=['return'])
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
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "vid"-------
    t = 0
    vidClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    movie = visual.MovieStim(win=win, name='movie',
        filename=stim,
        ori=0, pos=[0, 0], opacity=1,
        depth=0.0,
        )
#    key_resp_temp = event.BuilderKeyResponse()  # create an object of type KeyResponse
#    key_resp_temp.status = NOT_STARTED
    # keep track of which components have finished
    vidComponents = []
    vidComponents.append(movie)
#    vidComponents.append(key_resp_temp)
    for thisComponent in vidComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "vid"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = vidClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie* updates
        if t >= 0.0 and movie.status == NOT_STARTED:
            # keep track of start time/frame for later
            movie.tStart = t  # underestimates by a little under one frame
            movie.frameNStart = frameN  # exact frame index
            movie.setAutoDraw(True)
        if movie.status == FINISHED:  # force-end the routine
            continueRoutine = False
        
#        # *key_resp_temp* updates
#        if t >= 0.0 and key_resp_temp.status == NOT_STARTED:
#            # keep track of start time/frame for later
#            key_resp_temp.tStart = t  # underestimates by a little under one frame
#            key_resp_temp.frameNStart = frameN  # exact frame index
#            key_resp_temp.status = STARTED
#            # keyboard checking is just starting
#            key_resp_temp.clock.reset()  # now t=0
#            event.clearEvents()
#        if key_resp_temp.status == STARTED:
#            theseKeys = event.getKeys(keyList=['return'])
#            if len(theseKeys) > 0:  # at least one key was pressed
#                key_resp_temp.keys = theseKeys[-1]  # just the last key pressed
#                key_resp_temp.rt = key_resp_temp.clock.getTime()
#                # a response ends the routine
#                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in vidComponents:
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
    
    #-------Ending Routine "vid"-------
    for thisComponent in vidComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
#    # check responses
#    if key_resp_temp.keys in ['', [], None]:  # No response was made
#       key_resp_temp.keys=None
#    # store data for trials (TrialHandler)
#    trials.addData('key_resp_temp.keys',key_resp_temp.keys)
#    if key_resp_temp.keys != None:  # we had a response
#        trials.addData('key_resp_temp.rt', key_resp_temp.rt)
    
    #------Prepare to start Routine "quest"-------
    t = 0
    questClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image.setImage(question)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    questComponents = []
    questComponents.append(image)
    questComponents.append(response)
    for thisComponent in questComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "quest"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = questClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *response* updates
        if t >= 0.0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents()
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['a', 'b', 'c', 'd'])
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questComponents:
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
    
    #-------Ending Routine "quest"-------
    for thisComponent in questComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
       response.keys=None
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_end = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_end.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(thanks)
endComponents.append(key_resp_end)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if t >= 0.0 and thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks.tStart = t  # underestimates by a little under one frame
        thanks.frameNStart = frameN  # exact frame index
        thanks.setAutoDraw(True)
    
    # *key_resp_end* updates
    if t >= 0.0 and key_resp_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_end.tStart = t  # underestimates by a little under one frame
        key_resp_end.frameNStart = frameN  # exact frame index
        key_resp_end.status = STARTED
        # keyboard checking is just starting
        key_resp_end.clock.reset()  # now t=0
        event.clearEvents()
    if key_resp_end.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_end.keys = theseKeys[-1]  # just the last key pressed
            key_resp_end.rt = key_resp_end.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
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

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
