from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line

class DraggableWidget (RelativeLayout):
    def __init__(self, **kwargs):
        self.selected = None
        super(DraggableWidget, self).__init__(**kwargs)
        
    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.select()
            return True
        return super(DraggableWidget, self).on_touch_down(touch)
    
    def select(self):
        if not self.select:
            self.ix = self.center_x
            self.iy = self.center_y
            with self.canvas:
                self.selected = Line(rectangle=(0, 0, self.width, self.height), dash_offset = 2)
    
    def on_touch_move(self, touch):
        (x, y) = self.parent.to_parent(touch.x, touch.y)
        if self.selected and self.parent.collide_point(x - self.width/2, y - self.height/2):
            self.translate(touch.x-self.ix, touch.y-self.iy)
        return super(DraggableWidget, self).on_touch_move(touch)(self, touch)            
                