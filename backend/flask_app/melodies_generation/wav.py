from pydub import AudioSegment
import pyglet

def combine(file_name_one, file_name_two, file_name_combined):
    sound1= AudioSegment.from_file(file_name_one)
    sound2= AudioSegment.from_file(file_name_two)
    combined = sound1.overlay(sound2)

    combined.export(file_name_combined, format='wav')

def play(file_name):
    music = pyglet.resource.media(file_name)
    music.play()

    pyglet.app.run()


if __name__ == '__main__':
    # main_play('combined.wav', 'percusion_salsa.wav')
    pass
