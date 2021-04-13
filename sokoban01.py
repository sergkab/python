

def render(self):
     UCS.werase(self.win)
     for y in range(self.gmap_ref.height):
         for x in range(self.gmap_ref.width):
             if self.gmap_ref.tiles[x][y].owner == None:
                 pair = Renderer.MAP_DEFAULT_PAIR
             else:
                 pair = Renderer.PLAYERS_PAIRS[self.gmap_ref.tiles[x][y].owner.color]
             UCS.wattron(self.win, UCS.COLOR_PAIR(pair))
             scr_x, scr_y = self.real2screen(x, y)
             UCS.mvwaddstr(self.win,
                           scr_y,
                           scr_x,
                           self.gmap_ref.tiles[x][y].get_symbol() + " ")
             UCS.wattroff(self.win, UCS.COLOR_PAIR(pair))
     self.refresh()
     return
'''
aa=0
print ( aa )
print ("qqqq")
print ("2222")
'''
