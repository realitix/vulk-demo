#!/usr/bin/env python3.6
from vulk.baseapp import BaseApp
from vulk.graphic.d2.batch import TextBatch
from vulk.graphic.d2.fontdata import FontData


class App(BaseApp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start(self):
        super().start()
        self.data = FontData(self.context, '/home/realitix/git/vulk/vulk/asset/font/arial.fnt')
        self.batch = TextBatch(self.context)


    def end(self):
        pass

    def reload(self):
        pass

    def render(self, delta):
        # Clear screen
        self.context.clear_final_image([0, 0, 0.2, 1])

        self.batch.begin(self.context)
        self.batch.draw_char(self.data, "t", 10, 10, 100, 100)
        batch_semaphore = self.batch.end()
        self.context.swap([batch_semaphore])


def main():
    app = App(debug=True)
    with app as a:
        a.run()


if __name__ == "__main__":
    main()
