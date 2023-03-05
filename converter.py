from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import os
from moviepy.editor import *
from pydub import AudioSegment
from plyer import filechooser
from PIL import Image


class ConvertorMain(MDScreen):
    ...


class VideoConvertor(MDScreen):
    def check_file(self):
        filename = self.path

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.replace('.', '')

        if ext.lower() == self.ids.format.text:
            self.ids.format.text = ''

        if self.ids.format.text == 'mp3':
            self.to_mp3(video=filename)
        elif self.ids.format.text == 'mkv':
            self.to_mkv(video=filename)
        elif self.ids.format.text == 'wav':
            self.to_wav(video=filename)
        elif self.ids.format.text == 'ogg':
            self.to_ogg(video=filename)
        elif self.ids.format.text == 'mp4':
            self.to_mp4(video=filename)
        elif self.ids.format.text == 'm4a':
            self.to_m4a(video=filename)
        elif self.ids.format.text == '3g2':
            self.to_3g2(video=filename)
        elif self.ids.format.text == '3gp':
            self.to_3gp(video=filename)
        elif self.ids.format.text == '3gpp':
            self.to_3gpp(video=filename)
        elif self.ids.format.text == 'avi':
            self.to_avi(video=filename)
        elif self.ids.format.text == 'dv':
            self.to_dv(video=filename)
        elif self.ids.format.text == 'flac':
            self.to_flac(video=filename)
        elif self.ids.format.text == 'aac':
            self.to_aac(video=filename)
        elif self.ids.format.text == 'wma':
            self.to_wma(video=filename)
        elif self.ids.format.text == 'aiif':
            self.to_aiif(video=filename)
        elif self.ids.format.text == 'mov':
            self.to_mov(video=filename)
        elif self.ids.format.text == 'webm':
            self.to_webm(video=filename)
        elif self.ids.format.text == 'wmv':
            self.to_wmv(video=filename)
        elif self.ids.format.text == 'ts':
            self.to_ts(video=filename)
        elif self.ids.format.text == 'mpeg':
            self.to_mpeg(video=filename)
        elif self.ids.format.text == 'mpg':
            self.to_mpg(video=filename)
        else:
            error_dialog = Popup(title='Error',
                                 size_hint=(None, None),
                                 size=(400, 200))

            # Create a BoxLayout to hold the Label and Button widgets
            box_layout = BoxLayout(orientation='vertical')
            box_layout.add_widget(
                Label(text='Please enter a valid file format'))

            # Create the OK button and add it to the BoxLayout
            ok_button = Button(text="OK", size_hint=(
                None, None), size=(100, 50))
            ok_button.bind(on_press=error_dialog.dismiss)
            box_layout.add_widget(ok_button)

            # Add the BoxLayout to the content of the error dialog
            error_dialog.content = box_layout

            # Open the error dialog
            error_dialog.open()

    def file_chooser(self):
        path = filechooser.open_file()[0]
        self.path = path

    def clear_checkbox(self):
        self.path = ''
        self.ids.format.text = ''

    def to_mp3(self, video):
        clip = VideoFileClip(video)
        clip.audio.write_audiofile("audio.mp3")
        clip.close()
        self.clear_checkbox()

    def to_mkv(self, video):
        clip = VideoFileClip(video)
        clip.write_videofile("video.mkv")
        clip.close()
        self.clear_checkbox()

    def to_mp4(self, video):
        clip = VideoFileClip(video)
        clip.write_videofile("video.mp4")
        clip.close()
        self.clear_checkbox()

    def to_ogg(self, video):
        clip = VideoFileClip(video)
        clip.audio.write_audiofile("audio.ogg")
        clip.close()
        self.clear_checkbox()

    def to_wav(self, video):
        clip = VideoFileClip(video)
        audio = clip.audio
        audio.write_audiofile("audio.wav")
        clip.close()
        audio.close()
        self.clear_checkbox()

    def to_m4a(self, video):
        clip = AudioFileClip(video)
        clip.write_audiofile("output.m4a", codec='aac', buffersize=8192)
        clip.close()
        self.clear_checkbox()

    def to_3g2(self, video):
        clip = VideoFileClip(video)
        clip.write_videofile("output.3g2", codec="libx264",
                             audio_codec="aac", preset="ultrafast")
        clip.close()
        self.clear_checkbox()

    def to_3gp(self, video):
        video = VideoFileClip(video)
        video.write_videofile("video.3gp", codec='mpeg4',
                              audio_codec='libvo_aacenc')

    def to_3gpp(self, video):
        clip = VideoFileClip(video)
        clip.write_videofile("video.3gpp", codec='libx264', audio_codec='aac',
                             preset='ultrafast', ffmpeg_params=['-strict', '-2'])
        clip.close()
        self.clear_checkbox()

    def to_avi(self, video):
        clip = VideoFileClip(video)
        clip.write_videofile("video.avi")
        clip.close()
        self.clear_checkbox()

    def to_dv(self, video):
        clip = VideoFileClip(video)
        new_clip = clip.fx(vfx.maintain_ratio).fx(vfx.resize, width=720).set_fps(25).set_audio_fps(
            48000).set_audio_channels(2).set_audio_codec('pcm_s16le').set_video_codec('dvvideo')
        new_clip.write_videofile("video.dv", codec='rawvideo',
                                 audio_codec='pcm_s16le', fps=25, audio_fps=48000, audio_channels=2)
        clip.close()
        self.clear_checkbox()

    def to_flac(self, video):
        clip = VideoFileClip(video)
        audio = clip.audio

        # Write audio to output file in flac format
        audio.write_audiofile("audio.flac", codec="flac")
        clip.close()
        audio.close()
        self.clear_checkbox()

    def to_aac(self, video):
        clip = VideoFileClip(video)

        # Extract the audio from the video
        audio = clip.audio

        # Replace 'output_audio.aac' with the name you want to give your output file
        audio.write_audiofile('audio.aac')
        clip.close()
        audio.close()
        self.clear_checkbox()

    def to_wma(self, video):
        clip = VideoFileClip(video)

        # replace "output.wma" with the name of your output file
        clip.audio.write_audiofile("audio.wma", codec="wmav2")
        clip.close()
        self.clear_checkbox()

    def to_aiif(self, video):
        clip = VideoFileClip(video)
        clip.audio.write_audiofile("audio.aiff", codec="pcm_s16le")
        clip.close()
        self.clear_checkbox()

    def to_mov(self, video):
        clip = VideoFileClip(video)
        clip.write_videofile("video.mov", codec="mov")
        clip.close()
        self.clear_checkbox()

    def to_webm(self, video):
        clip = VideoFileClip(video)
        clip.write_videofile("video.webm", codec="libvpx",
                             audio_codec="libvorbis")
        clip.close()
        self.clear_checkbox()

    def to_wmv(self, video):
        clip = VideoFileClip(video)
        clip.write_videofile("video.wmv", codec="wmv2")
        clip.close()
        self.clear_checkbox()

    def to_ts(self, video):
        clip = VideoFileClip(video)

        # write video to output file in TS format
        clip.write_videofile("video.ts", codec='mpeg2video')
        clip.close()
        self.clear_checkbox()

    def to_mpeg(self, video):
        clip = VideoFileClip(video)

        # Convert the video to mpeg format
        clip.write_videofile("video.mpeg", codec='mpeg4')
        clip.close()
        self.clear_checkbox()

    def to_mpg(self, video):
        clip = VideoFileClip(video)

        clip.write_videofile("video.mpg", codec="mpeg")
        clip.close()
        self.clear_checkbox()


class AudioConvertor(MDScreen):
    def check_file(self):
        filename = self.path

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.replace('.', '')

        if ext.lower() == self.ids.audio_format.text:
            self.ids.audio_format.text = ''

        if self.ids.audio_format.text == 'mp3':
            self.to_mp3(audio=filename)
        elif self.ids.audio_format.text == 'aac':
            self.to_aac(audio=filename)
        elif self.ids.audio_format.text == 'ac3':
            self.to_ac3(audio=filename)
        elif self.ids.audio_format.text == 'aif':
            self.to_aif(audio=filename)
        elif self.ids.audio_format.text == 'aiff':
            self.to_aiff(audio=filename)
        elif self.ids.audio_format.text == 'amr':
            self.to_amr(audio=filename)
        elif self.ids.audio_format.text == 'au':
            self.to_au(audio=filename)
        elif self.ids.audio_format.text == 'caf':
            self.to_caf(audio=filename)
        elif self.ids.audio_format.text == 'flac':
            self.to_flac(audio=filename)
        elif self.ids.audio_format.text == 'm4a':
            self.to_m4a(audio=filename)
        elif self.ids.audio_format.text == 'm4b':
            self.to_m4b(audio=filename)
        elif self.ids.audio_format.text == 'oga':
            self.to_oga(audio=filename)
        elif self.ids.audio_format.text == 'voc':
            self.to_voc(audio=filename)
        elif self.ids.audio_format.text == 'wav':
            self.to_wav(audio=filename)
        elif self.ids.audio_format.text == 'weba':
            self.to_weba(audio=filename)
        elif self.ids.audio_format.text == 'wma':
            self.to_wma(audio=filename)
        else:
            error_dialog = Popup(title='Error',
                                 size_hint=(None, None),
                                 size=(400, 200))

            # Create a BoxLayout to hold the Label and Button widgets
            box_layout = BoxLayout(orientation='vertical')
            box_layout.add_widget(
                Label(text='Please enter a valid file format'))

            # Create the OK button and add it to the BoxLayout
            ok_button = Button(text="OK", size_hint=(
                None, None), size=(100, 50))
            ok_button.bind(on_press=error_dialog.dismiss)
            box_layout.add_widget(ok_button)

            # Add the BoxLayout to the content of the error dialog
            error_dialog.content = box_layout

            # Open the error dialog
            error_dialog.open()

    def file_chooser(self):
        path = filechooser.open_file()[0]
        self.path = path

    def clear_fields(self):
        self.path = ''
        self.ids.audio_format.text = ''

    def to_mp3(self, audio):
        audio_clip = AudioFileClip(audio)

        audio_clip.write_audiofile(
            "audio.mp3", fps=44100, codec='libmp3lame', bitrate='320k')

        audio_clip.close()
        self.clear_fields()

    def to_aac(self, audio):
        audio_clip = AudioFileClip(audio)

        audio_clip.write_audiofile(
            "audio.aac", fps=44100, codec='aac', bitrate='256k')
        audio_clip.close()

        self.clear_fields()

    def to_ac3(self, audio):
        audio_clip = AudioFileClip(audio)

        audio_clip.write_audiofile(
            "audio.ac3", fps=44100, codec='ac3', bitrate='448k')
        audio_clip.close()
        self.clear_fields()

    def to_aif(self, audio):
        audio_clip = AudioFileClip(audio)
        audio_clip.write_audiofile("audio.aif", fps=44100, codec='pcm_s16le')
        audio_clip.close()
        self.clear_fields()

    def to_aiff(self, audio):
        audio_clip = AudioFileClip(audio)
        audio_clip.write_audiofile("audio.aiff", fps=44100, codec='pcm_s16be')
        audio_clip.close()
        self.clear_fields()

    def to_amr(self, audio):
        input_audio = AudioFileClip(audio)

        input_audio.write_audiofile('audio.amr', codec='amr_nb')
        input_audio.close()
        self.clear_fields()

    def to_au(self, audio):
        audio_clip = AudioFileClip(audio)
        audio_clip.write_audiofile("audio.au")
        audio_clip.close()
        self.clear_fields()

    def to_caf(self, audio):
        input_audio = AudioFileClip(audio)
        input_audio.write_audiofile("audio.caf", codec='caf')
        input_audio.close()
        self.clear_fields()

    def to_flac(self, audio):
        audio_clip = AudioFileClip(audio)
        audio_clip.write_audiofile("audio.flac", codec='flac')
        audio_clip.close()
        self.clear_fields()

    def to_m4a(self, audio):
        input_file = AudioFileClip(audio)
        input_file.write_audiofile("audio.m4a", codec="aac")
        input_file.close()
        self.clear_fields()

    def to_m4b(self, audio):
        audio_clip = AudioFileClip(audio)
        audio_clip.write_audiofile("audio.m4b", codec='aac', bitrate='256k')
        audio_clip.close()
        self.clear_fields()

    def to_oga(self, audio):
        audio_clip = AudioFileClip(audio)
        audio_clip.write_audiofile("audio.oga", codec='libvorbis')
        audio_clip.close()
        self.clear_fields()

    def to_voc(self, audio):
        sound = AudioSegment.from_file(audio)
        sound.export("audio.voc", format="voc")
        self.clear_fields()

    def to_wav(self, audio):
        audio_clip = AudioFileClip(audio)
        audio_clip.write_audiofile("audio.wav", codec='pcm_s16le')
        audio_clip.close()
        self.clear_fields()

    def to_weba(self, audio):
        audio_clip = AudioFileClip(audio)
        audio_clip.write_audiofile("audio.weba", codec='libvorbis')
        audio_clip.close()
        self.clear_fields()

    def to_wma(self, audio):
        audio_clip = AudioFileClip(audio)
        audio_clip.write_audiofile("audio.wma", codec='wmav2')
        audio_clip.close()
        self.clear_fields()


class ImageConvertor(MDScreen):
    def check_file(self):
        filename = self.path

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.replace('.', '')

        if ext.lower() == self.ids.pic_format.text:
            self.ids.pic_format.text = ''

        if self.ids.pic_format.text == 'pdf':
            self.to_pdf(filename)
        elif self.ids.pic_format.text == 'svg':
            self.to_svg(filename)
        elif self.ids.pic_format.text == 'gif':
            self.to_gif(filename)
        elif self.ids.pic_format.text == 'jpeg':
            self.to_jpeg(filename)
        elif self.ids.pic_format.text == 'bmp':
            self.to_bmp(filename)
        elif self.ids.pic_format.text == 'xbm':
            self.to_xbm(filename)
        elif self.ids.pic_format.text == 'jp2':
            self.to_jp2(filename)

    def file_chooser(self):
        path = filechooser.open_file()[0]
        self.path = path

    def clear_text(self):
        self.path = ''
        self.ids.pic_format.text = ''

    def to_pdf(self, image_file):
        image = Image.open(image_file)

        image.save('image.pdf', 'PDF', resolution=100.0)
        image.close()
        self.clear_text()

    def to_svg(self, image_file):
        image = Image.open(image_file)
        image.save('image.svg', 'SVG')
        image.close()
        self.clear_text()

    def to_gif(self, image_file):
        image = Image.open(image_file)
        image.save("image.gif", 'GIF')
        image.close()
        self.clear_text()

    def to_jpeg(self, image_file):
        image = Image.open(image_file)
        image.save("image.jpeg", 'JPEG')
        image.close()
        self.clear_text()

    def to_bmp(self, image_file):
        image = Image.open(image_file)
        image.save("image.bmp", 'BMP')
        image.close()
        self.clear_text()

    def to_xbm(self, image_file):
        image = Image.open(image_file)
        image.save("image.xbm", 'XBM')
        image.close()
        self.clear_text()

    def to_jp2(self, image_file):
        image = Image.open(image_file)
        image.save("image.jp2", 'JPEG2000')
        image.close()
        self.clear_text()


Builder.load_file("Convertor.kv")
Builder.load_file("Audio.kv")
Builder.load_file("Video.kv")
Builder.load_file("Image.kv")


class Convertor(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.screen_manager = ScreenManager()
        self.Convertor_main = ConvertorMain()
        self.audioconvertor = AudioConvertor()
        self.videoconvertor = VideoConvertor()
        self.imageconvertor = ImageConvertor()
        self.screen_manager.add_widget(self.Convertor_main)
        self.screen_manager.add_widget(self.audioconvertor)
        self.screen_manager.add_widget(self.videoconvertor)
        self.screen_manager.add_widget(self.imageconvertor)

        return self.screen_manager

    def change(self, screen):
        self.screen_manager.current = screen


Convertor().run()
