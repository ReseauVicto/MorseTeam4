  from gpiozero import LED
  from time import sleep

  led = LED(17)

      led.on(0.5)
      sleep(0.2)
      led.on(0.5)
      sleep(0.2)
      led.on(0.5)
      sleep(0.2)
      led.on(0.5)
      led.off()
