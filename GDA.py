#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), Thu Nov 29 13:31:35 2012
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
expName='GDA_skeleton'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'001'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_GDA_%s' %(expInfo['participant'], expInfo['date'])
logFile=logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#an ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
datFile=open('data' + os.path.sep + '%s_GDA_%s.txt' %(expInfo['participant'], expInfo['date']),'a')
datFile.write('Trial\tFace1\tScene1\tFace2\tScene2\tProbe\tTrialType\tResponse\tTargets\tHits\tMisses\tFAs\tRT\n')

#setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb')

#Info about experiment length and counterbalancing
runLength=5
counterbalance=np.asarray((['f']+['s']+['b']+['p'])*3)
seed(int(expInfo['participant'])+18)
shuffle(counterbalance)
print 'counterbalance=%s'%(counterbalance)
runNum=len(counterbalance)
totTrialNum=runNum*runLength

#Initialise components for Routine "instr"
instrClock=core.Clock()
instructions=visual.TextStim(win=win, ori=0, name='instructions',
    text='Press ENTER to begin.',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

#Initialise components for other instructions
instr_f=visual.TextStim(win=win, ori=0, name='instructions',
    text='Remember faces, ignore scenes',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr_s=visual.TextStim(win=win, ori=0, name='instructions',
    text='Remember scenes, ignore faces',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr_b=visual.TextStim(win=win, ori=0, name='instructions',
    text='Remember both faces and scenes',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
instr_p=visual.TextStim(win=win, ori=0, name='instructions',
    text='Passive view',
    font='Arial',
    pos=[0, 0], height=0.1,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

#Initialise components for Routine "trial"
trialClock=core.Clock()
image1=visual.ImageStim(win=win, name='image1',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[225, 338],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
image2=visual.ImageStim(win=win, name='image2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[225, 338],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
image3=visual.ImageStim(win=win, name='image3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[225, 338],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)
image4=visual.ImageStim(win=win, name='image4',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[225, 338],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-3.0)
delay=visual.TextStim(win=win, ori=0, name='delay',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.2,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)
image5=visual.ImageStim(win=win, name='image5',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[225, 338],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-5.0)
ITI=visual.TextStim(win=win, ori=0, name='ITI',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.2,wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Create some handy timers
globalClock=core.Clock() #to track the time since experiment started
#routineTimer=core.CountdownTimer() #to track time remaining of each (non-slip) routine 

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
        theseKeys = event.getKeys(keyList=['return', '+'])
        if len(theseKeys)>0:#at least one key was pressed
            instr_resp.keys=theseKeys[-1]#just the last key pressed
            instr_resp.rt = instr_resp.clock.getTime()
            #abort routine on response
            continueRoutine=False
    
    #check if all components have finished
    if not continueRoutine: #a component has requested that we end
#        routineTimer.reset() #this is the new t0 for non-slip Routines
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
varLists=np.loadtxt('conditions.txt',dtype='str',delimiter='\t')  #loads info from conditions file (which should be a .txt not an .xlsx)
femFaces=varLists[0:90,0]
malFaces=varLists[90:180,0]
sceneList=varLists[:,1]
arrows=varLists[:,2]
seed(int(expInfo['participant'])+65) #seeds randomization based on participant number
shuffle(femFaces)  #shuffles/randomizes list based on above seed
seed(int(expInfo['participant'])+47) #seeds randomization based on participant number
shuffle(malFaces)  #shuffles/randomizes list based on above seed
seed(int(expInfo['participant'])+94) #seeds randomization based on participant number
shuffle(sceneList)  #shuffles/randomizes list based on above seed
male1=malFaces[0:totTrialNum/2]
male2=malFaces[totTrialNum/2:totTrialNum]
male_rest=malFaces[totTrialNum:len(malFaces)]
female1=femFaces[0:totTrialNum/2]
female2=femFaces[totTrialNum/2:totTrialNum]
female_rest=femFaces[totTrialNum:len(femFaces)]
sceneList1=sceneList[0:totTrialNum]
sceneList2=sceneList[totTrialNum:totTrialNum*2]
scenes_rest=sceneList[totTrialNum*2:len(sceneList)]
order=[]
for i in range(len(counterbalance)):
    if counterbalance[i]=='p':
        order.extend([0]*runLength)
    else:
        this_order=[0]*int(runLength*0.8)+[1]*int(runLength*0.2)
        seed(int(expInfo['participant'])+93+i)
        shuffle(this_order)
        order.extend(this_order)
faceList1=[]
faceList2=[]
target=[]
trialType=[]
for i in range(totTrialNum):
    rangemat=(range(0,runNum*runLength,runLength))+(range(runLength,(runNum+1)*runLength,runLength))
    rangemat=np.sort(rangemat)
    rangemat=np.reshape(rangemat, (runNum,-1))
    a1=i>=rangemat[:,0]
    a2=i<rangemat[:,1]
    b=a1*a2
    idx=np.where(b)
    this_cb=counterbalance[idx]
    trialType.append(this_cb)
    malvsfem=[0]*int(totTrialNum/2)+[1]*int(totTrialNum/2)
    seed(int(expInfo['participant'])+15)
    shuffle(malvsfem)
    seed(int(expInfo['participant'])+i+12)
    firstorsecond=np.random.randint(0,100)
    faceorscene=np.random.randint(0,100)
    RorL=np.random.randint(0,100)
    if malvsfem[i]==0: #male faces
        faceList1.append(male1[0])
        faceList2.append(male2[0])
        if this_cb=='f': #face condition
            if order[i]==0:
                target.append(male_rest[0])
                male_rest=np.delete(male_rest,0)
            elif order[i]==1:
                firstorsecond=np.random.randint(0,100)
                if firstorsecond<50:
                    target.append(male1[0])
                else:
                    target.append(male2[0])
        elif this_cb=='b' and faceorscene<50: #both, face target
            if order[i]==0:
                target.append(male_rest[0])
                male_rest=np.delete(male_rest,0)
            elif order[i]==1:
                if firstorsecond<50:
                    target.append(male1[0])
                else:
                    target.append(male2[0])
        male1=np.delete(male1,0)
        male2=np.delete(male2,0)
    elif malvsfem[i]==1: #female faces
        faceList1.append(female1[0])
        faceList2.append(female2[0])
        if this_cb=='f': #face condition
            if order[i]==0:
                target.append(female_rest[0])
                female_rest=np.delete(female_rest,0)
            elif order[i]==1:
                if firstorsecond<50:
                    target.append(female1[0])
                else:
                    target.append(female2[0])
        elif this_cb=='b' and faceorscene<50: #both, face target
            if order[i]==0:
                target.append(female_rest[0])
                female_rest=np.delete(female_rest,0)
            elif order[i]==1:
                if firstorsecond<50:
                    target.append(female1[0])
                else:
                    target.append(female2[0])
        female1=np.delete(female1,0)
        female2=np.delete(female2,0)
    if this_cb=='b' and faceorscene>=50: #both, scene target
        if order[i]==0:
            target.append(scenes_rest[0])
            scenes_rest=np.delete(scenes_rest,0)
        elif order[i]==1:
            if firstorsecond<50:
                target.append(sceneList1[i])
            else:
                target.append(sceneList2[i])
    elif this_cb=='s': #scene condition
        if order[i]==0:
            target.append(scenes_rest[0])
            scenes_rest=np.delete(scenes_rest,0)
        elif order[i]==1:
            if firstorsecond<50:
                target.append(sceneList1[i])
            else:
                target.append(sceneList2[i])
    elif this_cb=='p': #passive condition
        if RorL<50:
            target.append(arrows[0])
        else:
            target.append(arrows[1])
myarray = []
for i in range(len(order)):
    myarray.append({'face1': faceList1[i], 'scene1': sceneList1[i], 'face2': faceList2[i], 'scene2': sceneList2[i], 'target': target[i], 'order': order[i], 'trialType_index': i}) #puts data into an array of dictionaries that the TrialHandler function will accept
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
instrScreens=[]
for x in range(1,runNum):
    instrScreens.append(runLength*x)
instrScreens=[0]+instrScreens
for thisTrial in trials:
    
    if trials.thisTrialN in instrScreens:
        
        if trialType[trialType_index+1]=='f':
            instr_f.draw()
        elif trialType[trialType_index+1]=='s':
            instr_s.draw()
        elif trialType[trialType_index+1]=='b':
            instr_b.draw()
        elif trialType[trialType_index+1]=='p':
            instr_p.draw()
        win.flip()
        event.waitKeys(keyList=['return','+'])
    
    currentLoop = trials
    #abbrieviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial!=None:
        for paramName in thisTrial.keys():
            exec(paramName+'=thisTrial.'+paramName)
    
    #------Prepare to start Routine"trial"-------
    t=0; trialClock.reset() #clock 
    frameN=-1
#    routineTimer.add(7.200000)
    #update component parameters for each repeat
    image1.setImage(face1)
    image2.setImage(scene1)
    image3.setImage(face2)
    image4.setImage(scene2)
    image5.setImage(target)
    targ_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    targ_resp.status=NOT_STARTED
    #keep track of which components have finished
    trialComponents=[]
    trialComponents.append(image1)
    trialComponents.append(image2)
    trialComponents.append(image3)
    trialComponents.append(image4)
    trialComponents.append(delay)
    trialComponents.append(image5)
    trialComponents.append(targ_resp)
    trialComponents.append(ITI)
    for thisComponent in trialComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
    #-------Start Routine "trial"-------
    continueRoutine=True
    while continueRoutine:# and routineTimer.getTime()>0:
        #get current time
        t=trialClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
        
        #*image1* updates
        if t>=0.0 and image1.status==NOT_STARTED:
            #keep track of start time/frame for later
            image1.tStart=t#underestimates by a little under one frame
            image1.frameNStart=frameN#exact frame index
            image1.setAutoDraw(True)
        elif image1.status==STARTED and t>=(0.0+0.8):
            image1.setAutoDraw(False)
        
        #*image2* updates
        if t>=0.8 and image2.status==NOT_STARTED:
            #keep track of start time/frame for later
            image2.tStart=t#underestimates by a little under one frame
            image2.frameNStart=frameN#exact frame index
            image2.setAutoDraw(True)
        elif image2.status==STARTED and t>=(0.8+0.8):
            image2.setAutoDraw(False)
        
        #*image3* updates
        if t>=1.6 and image3.status==NOT_STARTED:
            #keep track of start time/frame for later
            image3.tStart=t#underestimates by a little under one frame
            image3.frameNStart=frameN#exact frame index
            image3.setAutoDraw(True)
        elif image3.status==STARTED and t>=(1.6+0.8):
            image3.setAutoDraw(False)
        
        #*image4* updates
        if t>=2.4 and image4.status==NOT_STARTED:
            #keep track of start time/frame for later
            image4.tStart=t#underestimates by a little under one frame
            image4.frameNStart=frameN#exact frame index
            image4.setAutoDraw(True)
        elif image4.status==STARTED and t>=(2.4+0.8):
            image4.setAutoDraw(False)
        
        #*delay* updates
        if t>=3.2 and delay.status==NOT_STARTED:
            #keep track of start time/frame for later
            delay.tStart=t#underestimates by a little under one frame
            delay.frameNStart=frameN#exact frame index
            delay.setAutoDraw(True)
        elif delay.status==STARTED and t>=(3.2+1.0):
            delay.setAutoDraw(False)
        
        #*image5* updates
        if t>=4.2 and image5.status==NOT_STARTED:
            #keep track of start time/frame for later
            image5.tStart=t#underestimates by a little under one frame
            image5.frameNStart=frameN#exact frame index
            image5.setAutoDraw(True)
        elif image5.status==STARTED and t>=(4.2+1.0):
            image5.setAutoDraw(False)
        
        #*ITI* updates
        if t>=5.2 and ITI.status==NOT_STARTED:
            #keep track of start time/frame for later
            ITI.tStart=t#underestimates by a little under one frame
            ITI.frameNStart=frameN#exact frame index
            ITI.setAutoDraw(True)
        elif ITI.status==STARTED and t>=(5.2+2.0):
            ITI.setAutoDraw(False)
        
        #*targ_resp* updates
        if t>=4.2 and targ_resp.status==NOT_STARTED:
            #keep track of start time/frame for later
            targ_resp.tStart=t#underestimates by a little under one frame
            targ_resp.frameNStart=frameN#exact frame index
            targ_resp.status=STARTED
            #keyboard checking is just starting
            targ_resp.clock.reset() # now t=0
            event.clearEvents()
        elif targ_resp.status==STARTED and t>=(4.2+1.5):
            targ_resp.status=STOPPED
        if targ_resp.status==STARTED:#only update if being drawn
            theseKeys = event.getKeys(keyList=['1', '2'])
            if len(theseKeys)>0:#at least one key was pressed
                targ_resp.keys=theseKeys[-1]#just the last key pressed
                targ_resp.rt = targ_resp.clock.getTime()
        
        #check if all components have finished
        if not continueRoutine: #a component has requested that we end
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
    if len(targ_resp.keys)==0: #No response was made
       targ_resp.keys=None
    #store data for trials (TrialHandler)
    trials.addData('targ_resp.keys',targ_resp.keys)
    if targ_resp.keys != None:#we had a response
        trials.addData('targ_resp.rt',targ_resp.rt)
    thisExp.nextEntry()

#completed 1 repeats of 'trials'
    if trialType[trialType_index]=='p':
        if target=='Stim/arrow_l.jpg':
            if targ_resp.keys=='1':
                hits=1
            else:
                hits=0
            if targ_resp.keys=='2':
                misses=1
            else:
                misses=0
        elif target=='Stim/arrow_r.jpg':
            if targ_resp.keys=='2':
                hits=1
            else:
                hits=0
            if targ_resp.keys=='1':
                misses=1
            else:
                misses=0
        FAs='N/A'
    else:
        if order==1 and targ_resp.keys=='1':
            hits=1
        else:
            hits=0
        if order==1 and targ_resp.keys!='1':
            misses=1
        else:
            misses=0
        if order==0 and targ_resp.keys=='1':
            FAs=1
        else:
            FAs=0
    datFile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(trials.thisTrialN+1,face1,scene1,face2,scene2,target,trialType[trialType_index],targ_resp.keys,order,hits,misses,FAs,targ_resp.rt))
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
