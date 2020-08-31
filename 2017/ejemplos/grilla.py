from wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame(None, -1, "")
        g = self.g = grid.Grid(f, -1)

        g.CreateGrid(20, 6)

        g.SetCellValue(0, 0, "Enter tipo TAB")
        g.SetCellValue(0, 5, "Enter onda editor")
        g.SetColSize(0, 150)
        g.SetColSize(5, 150)

        g.Bind(EVT_KEY_DOWN, self.OnKeyDown)
        f.Show()
        return True

    def OnKeyDown(self, evt):
        if evt.GetKeyCode() != WXK_RETURN:
            evt.Skip()
            return

        if evt.ControlDown():   # el edit control necesita esta movida
            evt.Skip()
            return

        self.g.DisableCellEditControl()
        success = self.g.MoveCursorRight(evt.ShiftDown())

        if not success:
            newRow = self.g.GetGridCursorRow() + 1

            if newRow < self.g.GetTable().GetNumberRows():
                self.g.SetGridCursor(newRow, 0)
                self.g.MakeCellVisible(newRow, 0)
            else:
                # nueva fila?
                # ver !
                pass

app = MiApp()
app.MainLoop()
