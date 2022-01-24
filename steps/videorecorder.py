from datetime import datetime
import os
import time

from subprocess import call

from radish import before, after, world


CMD = 'videorecording'


class SubTitles:

    def __init__(self, name):
        self.name = name
        self.text = None
        self.started = False
        self.startofvideo = False
        self.index = 0

    def start(self, text):
        if self.started:
            self._writenow()

        self.text = text
        self.started = datetime.now() - self.startofvideo

    def stop(self):
        self._writenow()
        self.started = False

    def _writenow(self):
        self._write(
            self.started,
            datetime.now() - self.startofvideo)

    def _write(self, start, stop):
        self.index += 1
        start = _formatdelta(start)
        stop = _formatdelta(stop)

        fn = os.path.join(world.config.user_data['reportsdir'], "{}.srt".format(self.name))
        with open(fn, "a") as srtfile:
            srtfile.writelines([
                '\n',
                '{}\n'.format(self.index),
                "{} --> {}\n".format(start, stop),
                '<b>{}</b>\n<i>{}</i>\n{}\n'.format(_blue(world.vr.feature), world.vr.scenario, self.text)])
            srtfile.close()


class VideoRecorder:

    def __init__(self, name):
        self.started = False
        self.name = name
        self.subtitles = SubTitles(self.name)

    def start(self):
        if self.started:
            return
        print("starting video recording for %s to %s"
              % (self.name, world.config.user_data['reportsdir']))
        self.started = datetime.now()
        call([CMD,
              "start",
              os.environ["DISPLAY"],
              world.config.user_data['reportsdir'],
              # 'reports/',
              self.name])
        self.subtitles.startofvideo = self.started

    def stop(self):
        print("stopping video recording for %s" % self.name)
        self.started = False
        call([CMD,
              "stop",
              os.environ["DISPLAY"],
              world.config.user_data['reportsdir'],
              self.name])


@before.each_step
def subtitle_step(step):
    world.vr.subtitles.start("step: " + step.sentence)
    time.sleep(0.5)


@before.each_scenario
def subtitle_scenario(scenario):
    world.vr.scenario = scenario.sentence
    world.vr.subtitles.start("scenario started")
    time.sleep(1)


@after.each_scenario
def subtitle_scenario_result(scenario):
    world.vr.subtitles.start("{} scenario: {}".format(scenario.state, scenario.sentence))
    time.sleep(1)


@before.each_feature
def start_videorecording(feature):
    fn = _feature2name(feature)
#   print(feature.line)
#   print(feature.sentence)
#   print(feature.keyword)
#   print(feature.description)
#   print(feature.path)
    print("start video recording for '%s'" % fn)
    world.vr = VideoRecorder(fn)
    world.vr.start()
    world.vr.feature = fn
    world.vr.subtitles.start("feature: " + _feature2name(feature))


@after.each_feature
def stop_videorecording(feature):
    fn = _feature2name(feature)
    print("*** stop video recording for '%s'" % fn)
    if not world.vr or not world.vr.started:
        return
    world.vr.subtitles.start("{} feature: {}".format(feature.state, fn))
    time.sleep(1)
    world.vr.subtitles.stop()
    world.vr.stop()


def _feature2name(feature):
    return os.path.basename(feature.path)


def _formatdelta(timedelta):
    # return timedelta.strftime("%H:%M:%S,%fff")
    TFT = "%02d:%02d:%02d,%03d"
    return TFT % (
        timedelta.seconds // 3600,
        timedelta.seconds % 3600 // 60,
        timedelta.seconds % 3600 % 60,
        timedelta.microseconds // 1000)


def _colorize(color, text):
    # return '<font color={}>x{}</font>'.format(color, text)
    return text


def _orange(text):
    return _colorize("#999922", text)


def _blue(text):
    return _colorize("#2222ee", text)
