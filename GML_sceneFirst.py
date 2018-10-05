#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), Mon Jul 23 18:00:53 2012
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
#import GML_retrieval

#store info about the experiment session
expName='ArimIdea'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'001'}
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
    savePickle=True, saveWideText=True,
    dataFileName=filename)
datFile=open('data' + os.path.sep + '%s_%s.txt' %(expInfo['participant'], expInfo['date']),'a')
datFile.write('Trial\tRun\tFace\tScene\tAttended\tstimOnset\tRT\n')

runNum=1
totRuns=6
totStimNum=120
sceneAttend=[1,3,5]
faceAttend=[2,4,6]
while runNum<=totRuns:
    if np.any(np.array(faceAttend) == runNum):
        instr_text='FACES'
        instr_text2='face'
    elif np.any(np.array(sceneAttend) == runNum):
        instr_text='SCENES'
        instr_text2='scene'
#    datFile=open('data' + os.path.sep + '%s_%s.txt' %(expInfo['participant'], expInfo['date']),'a')
#    datFile.write('Trial\tFace\tScene\tstimOnset\tRT\n')
    
    #setup the Window
    win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
        monitor='testMonitor', color='black', colorSpace='rgb')
    
    #Initialise components for Routine "instr"
    instrClock=core.Clock()
    text=visual.TextStim(win=win, ori=0, name='text',
        text='Remember %s\n\nPress spacebar when you first distinguish a %s. Press enter to begin.' % (instr_text,instr_text2),
        font='Arial',
        pos=[0, 0], height=0.1,wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    begExpClock=core.Clock()
    #Initialise components for Routine "fixScr"
    fixScrClock=core.Clock()
    
    fixation=visual.ImageStim(win=win, name='fixation',
        image=u'Stim' + os.path.sep + 'fixation.jpg', mask=None, units=u'pix',
        ori=0, pos=[0, 0], size=[256, 256],
        color=[1,1,1], colorSpace=u'rgb', opacity=1,
        texRes=128, interpolate=True, depth=-1.0)
    
    #Initialise components for Routine "trial"
    RTclock=core.Clock()
    trialClock=core.Clock()
    image1=visual.ImageStim(win=win, name='image1',units=u'pix', 
        image='sin', mask=None,
        ori=0, pos=[0, 0], size=[225, 338],
        color=[1,1,1], colorSpace=u'rgb', opacity=1,
        texRes=128, interpolate=True, depth=0.0)
    image2=visual.ImageStim(win=win, name='image2',units=u'pix', 
        image='sin', mask=None,
        ori=0, pos=[0, 0], size=[225, 338],
        color=[1,1,1], colorSpace=u'rgb', opacity=1,
        texRes=128, interpolate=True, depth=-1.0)
    imageF=visual.ImageStim(win=win, name='imageF',units=u'pix',
        image=u'Stim' + os.path.sep + 'fixation.jpg', mask=None,
        ori=0, pos=[0, 0], size=[256, 256],
        color=[1,1,1], colorSpace=u'rgb', opacity=1,
        texRes=128, interpolate=True, depth=-1.0)
    responseClock=core.Clock()
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
    
    #***set up handler to look after randomisation of conditions etc
    stimLists=np.loadtxt('conditions3.txt',dtype='str',delimiter='\t')  #loads info from conditions file (which should be a .txt not an .xlsx)
    fixes=stimLists[:,2]  #chooses column for each category of data
    faceList=stimLists[:,0]
    sceneList=stimLists[:,1]
    seed(int(expInfo['participant'])+65) #seeds randomization based on participant number
    shuffle(faceList)  #shuffles/randomizes list based on above seed
    seed(int(expInfo['participant'])+43) #seeds randomization based on participant number
    shuffle(sceneList)
    runLength=(totStimNum/totRuns)
    if runNum==1:
        faces=faceList[0:runLength] #picks the first 120 from the randomized list of total faces/scenes
        scenes=sceneList[0:runLength]
    elif runNum>1:
        faces=faceList[((runNum-1)*runLength):(runLength*runNum)] #picks the first 120 from the randomized list of total faces/scenes
        scenes=sceneList[((runNum-1)*runLength):(runLength*runNum)]
    myarray = []
    for i in range(len(faces)):
        myarray.append({'faces': faces[i], 'scenes': scenes[i], 'fixes': fixes[i]}) #puts data into an array of dictionaries that the TrialHandler function will accept
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
    counter = 0
    x = 20*np.array(range(1,180))
    begExpClock.reset()
    for thisTrial in trials:
        currentLoop = trials
        #abbrieviate parameter names if possible (e.g. rgb=thisTrial.rgb)
        if thisTrial!=None:
            for paramName in thisTrial.keys():
                exec(paramName+'=thisTrial.'+paramName)
        
        #------Prepare to start Routine"fixScr"-------
        t=0; fixScrClock.reset() #clock 
        frameN=-1
        #update component parameters for each repeat
        durr = randint(3,8)
        image1.setImage(faces)
        image2.setImage(scenes)
        #keep track of which components have finished
        fixScrComponents=[]
        fixScrComponents.append(fixation)
        for thisComponent in fixScrComponents:
            if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
        #-------Start Routine "fixScr"-------
        continueRoutine=True
        while continueRoutine:
            #get current time
            t=fixScrClock.getTime()
            frameN=frameN+1#number of completed frames (so 0 in first frame)
            #update/draw components on each frame
            
            
            #*fixation* updates
            if t>=0.0 and fixation.status==NOT_STARTED:
                #keep track of start time/frame for later
                fixation.tStart=t#underestimates by a little under one frame
                fixation.frameNStart=frameN#exact frame index
                fixation.setAutoDraw(True)
            elif fixation.status==STARTED and t>=(0.0+durr):
                fixation.setAutoDraw(False)
                fixOff=begExpClock.getTime()
            
            #check if all components have finished
            if not continueRoutine: #a component has requested that we end
                routineTimer.reset() #this is the new t0 for non-slip Routines
                break
            continueRoutine=False#will revert to True if at least one component still running
            for thisComponent in fixScrComponents:
                if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                    continueRoutine=True; break#at least one component has not yet finished
            
            #check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            #refresh the screen
            if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #End of Routine "fixScr"
        for thisComponent in fixScrComponents:
            if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
        
        RTclock.reset()
        #set up handler to look after randomisation of conditions etc
        trials_2=data.TrialHandler(nReps=20, method=u'random', 
            extraInfo=expInfo, originPath=None,
            trialList=[None],
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)#add the loop to the experiment
        thisTrial_2=trials_2.trialList[0]#so we can initialise stimuli with some values
        #abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
        if thisTrial_2!=None:
            for paramName in thisTrial_2.keys():
                exec(paramName+'=thisTrial_2.'+paramName)
        responseClock.reset()
        trialResponseTime='NaN'
        trialResponseKey=[]
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            #abbrieviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
            if thisTrial_2!=None:
                for paramName in thisTrial_2.keys():
                    exec(paramName+'=thisTrial_2.'+paramName)
            
            #------Prepare to start Routine"trial"-------
            t=0; trialClock.reset() #clock 
            frameN=-1
            counter= counter + 1 #sets up a counter for the total number of repetitions that goes through the trials_2 loop (counter does not reset when a new trials_2 loop starts)
            #update component parameters for each repeat
            key_resp_2 = event.BuilderKeyResponse() #create an object of type KeyResponse
            key_resp_2.status=NOT_STARTED
            #keep track of which components have finished
            trialComponents=[]
            trialComponents.append(key_resp_2)
            trialComponents.append(image1)
            trialComponents.append(image2)
            for thisComponent in trialComponents:
                if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
            #-------Start Routine "trial"-------
            continueRoutine=True
            while continueRoutine:
                #get current time
                t=trialClock.getTime()
                frameN=frameN+1#number of completed frames (so 0 in first frame)
                #update/draw components on each frame
                
                #*key_resp_2* updates
                if t>=fixation.status==FINISHED and key_resp_2.status==NOT_STARTED:
                    #keep track of start time/frame for later
                    key_resp_2.tStart=t#underestimates by a little under one frame
                    key_resp_2.frameNStart=frameN#exact frame index
                    key_resp_2.status=STARTED
                    #keyboard checking is just starting
                    key_resp_2.clock.reset() # now t=0
    #                event.clearEvents()
                elif key_resp_2.status==STARTED and t>=(fixation.status==FINISHED+2.3):
                    key_resp_2.status=STOPPED
                if key_resp_2.status==STARTED:#only update if being drawn
                    theseKeys = event.getKeys(keyList=['space'])
                    if len(theseKeys)>0:#at least one key was pressed
                        key_resp_2.keys.extend(theseKeys)#storing all keys
                        key_resp_2.rt.append(key_resp_2.clock.getTime())
                        key_resp.keys=theseKeys[0]#just the first key pressed
    #                    key_resp_2.rt = key_resp_2.clock.getTime()
                        trialResponseTime=RTclock.getTime()
                        trialResponseKey=theseKeys[-1]
                
                # this sets it up so that the very last trial in trials_2 loop is a fixation cross instead of one of the images (because there is a lag when moving on to the next routine and we don't want the last image being displayed for the duration of that lag)
                if np.any(np.array(x) == counter):
                    imageF.tStart=t#underestimates by a little under one frame
                    imageF.frameNStart=frameN#exact frame index
                    imageF.setAutoDraw(True)
                elif np.any(np.array(x) != counter):
                    imageF.setAutoDraw(False)
                
                #*image1* updates
                if frameN>=0.0 and image1.status==NOT_STARTED:
                    if np.any(np.array(x) == counter):
                        image1.setAutoDraw(False)
                        image1.status=FINISHED
                    elif np.any(np.array(x) != counter):
                        #keep track of start time/frame for later
                        image1.tStart=t#underestimates by a little under one frame
                        image1.frameNStart=frameN#exact frame index
                        image1.setAutoDraw(True)
                elif image1.status==STARTED and frameN>=3:
                    image1.setAutoDraw(False)
                
                #*image2* updates
                if frameN>=3 and image2.status==NOT_STARTED:
                    if np.any(np.array(x) == counter):
                        image2.setAutoDraw(False)
                        image2.status=FINISHED
                    elif np.any(np.array(x) != counter):
                        #keep track of start time/frame for later
                        image2.tStart=t#underestimates by a little under one frame
                        image2.frameNStart=frameN#exact frame index
                        image2.setAutoDraw(True)
                elif image2.status==STARTED and frameN>=6:
                    image2.setAutoDraw(False)
                        
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
        if len(trialResponseKey)==0: #No response was made
           trialResponseKey=None
        trials.addData('respKey', trialResponseKey)
        if trialResponseKey != []:#we had a response
            trials.addData('key_resp_rt',trialResponseTime)
        trials.addData('stimOnset',fixOff)
        trials.addData('Run',runNum)
        datFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(trials.thisTrialN+1,runNum,thisTrial.faces,thisTrial.scenes,instr_text2,fixOff,trialResponseTime))
        
#    datFile.close()
    runNum=runNum+1
    
    #get names of stimulus parameters
    if trials.trialList in ([], [None], None):  params=[]
    else:  params = trials.trialList[0].keys()
datFile.close()

#save data for this loop
#trials.saveAsPickle(filename+'trials', fileCollisionMethod='rename')
#trials.saveAsExcel(filename+'.xlsx', sheetName='trials',
#    stimOut=params,
#    dataOut=['n','all_mean','all_std', 'all_raw'])

#if expInfo['session']<4 and thisTrial_2>=2:
#    import GML_retrieval#(expInfo['participant'],(expInfo['session']+1))
#    #GML_retrieval(expInfo['participant'],(expInfo['session']+1))
#else:
#    win.close() 
#    core.quit()

#Shutting down:
win.close()
core.quit()
