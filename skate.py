import viz
import vizshape
import vizinfo
import vizact
import vizproximity

viz.setMultiSample(4)
viz.fov(60)
viz.go()

#adding the environment 
skatepark=viz.add('skatexone.osgb')

# Create proximity manager
manager = vizproximity.Manager()
manager.setDebug(True)

#setting up camera point of view
viz.MainView.setPosition([-15.48202, 4.71183, -0.30281])
viz.MainView.lookAt([-2.00242, 5.09411, -4.66583])

#declaring the avatars 
will=skatepark.getChild('will')
daniel=skatepark.getChild('daniel')
jordan=skatepark.getChild('jordan')
calvin=skatepark.getChild('calvin')
shakira=skatepark.getChild('shakira')

will.state(6)
daniel.state(6)

jordan.state(2)

calvin.state(3)
shakira.state(3)

# Add main viewpoint as proximity target
target = vizproximity.Target(viz.MainView)
manager.addTarget(target)

# Create sensor using bounding box of node
node = viz.addChild('speak.osgb')
sensor = vizproximity.addBoundingBoxSensor(node)
manager.addSensor(sensor)


#Add the sound
sound = viz.addAudio('sounds/platform_start.wav')

#function
def WhenEnter(e):
	sound.play()

def WhenExit(e):
	sound.stop
	
manager.onEnter(sensor,WhenEnter)

manager.onExit(sensor,WhenExit)

action=vizact.walkTo(pos=[-10.78322, 0, 1.16105])
jordan.runAction(action)

