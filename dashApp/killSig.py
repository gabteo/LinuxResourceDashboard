import signal
import logging

class killSig:
  def __init__(self):
    self.log = logging.getLogger(__name__)
    self.kill_now = False
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    self.log.info("Terminando programa...")
    self.kill_now = True