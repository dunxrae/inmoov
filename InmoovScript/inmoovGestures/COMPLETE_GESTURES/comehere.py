def comehere():
  fullspeed()
  rest()
  #neopixel.setAnimation("Larson Scanner", 0, 200, 0, 1)
##look around
  i01.setHeadSpeed(0.80, 0.80, 0.90, 0.90, 1.0)
  i01.moveHead(80,66,7,85,52)
  sleep(3)
  i01.moveHead(80,110,175,85,52)
  sleep(3)
##raise arm point finger
  i01.setHandSpeed("left", 0.85, 0.85, 0.85, 0.85, 0.85, 1.0)
  i01.setHandSpeed("right", 1.0, 0.85, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.90, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 0.90)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(80,86,85,85,52)
  i01.moveArm("left",5,94,30,10)
  i01.moveArm("right",7,74,92,10)
  i01.moveHand("left",180,180,180,180,180,90)
  i01.moveHand("right",180,2,175,160,165,180)
  i01.moveTorso(90,90,90)
  sleep(4.5)
##move finger
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(80,86)
  i01.moveArm("left",5,94,30,10)
  i01.moveArm("right",48,74,92,10)
  i01.moveHand("left",180,180,180,180,180,90)
  i01.moveHand("right",180,2,175,160,165,20)
  i01.moveTorso(90,90,90)
  sleep(2)
  i01.setHeadSpeed(0.80, 0.80)
  i01.moveHead(80,80)
  i01.moveHand("right",180,164,175,160,165,20)
  sleep(1)
  i01.moveHead(80,80)
  i01.moveHand("right",180,2,175,160,165,20)
  sleep(1)
  i01.moveHead(118,80)
  i01.moveHand("right",180,164,175,160,165,20)
  sleep(1)
  i01.mouth.speak("come closer")
  i01.moveHead(60,80)
  i01.moveHand("right",180,2,175,160,165,20)
  sleep(1)
  i01.moveHead(118,80)
  i01.moveHand("right",180,164,175,160,165,20)
  sleep(1)
  i01.moveHead(60,80)
  i01.moveArm("right",90,65,10,25)
  sleep(3)
  fullspeed()
  rest()
  sleep(0.3)
  relax()
  sleep(3)
  fullspeed()


