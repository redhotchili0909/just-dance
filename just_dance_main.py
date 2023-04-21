from just_dance_model import JustDanceModel
from just_dance_view import JustDanceView
from just_dance_controller import JustDanceController


class JustDanceGame:
    def __init__(self, model_path, video_path, camera_index):
        self.model = JustDanceModel(model_path=model_path)
        self.view = JustDanceView(model=self.model)
        self.controller = JustDanceController(model=self.model,
                                              video_path=video_path,
                                              camera_index=camera_index)

    def release_capture(self):
        self.cap1.release()
        self.cap2.release()

    def close_windows(self):
        self.controller.close_windows()

    def run(self):
        self.controller.process_frames()
        self.release_capture()
        self.close_windows()


if __name__ == "__main__":
    # Instantiate JustDanceApp with model path, video path, and camera index
    game = JustDanceGame(
        model_path="model.tflite", video_path="test.mp4", camera_index=0
    )
    game.run()
