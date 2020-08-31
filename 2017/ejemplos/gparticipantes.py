import wx
import wx.dataview as dv
import musdat

musicdata = musdat.musicdata.items()
musicdata.sort()
musicdata = [[str(k)] + list(v) for k,v in musicdata]


class MiApp(wx.App):
    def OnInit(self):
        f = wx.Frame(None, -1, "", size = (600,400))
        p = wx.Panel(f, -1)
        self.dvlc = dvlc = dv.DataViewListCtrl(p)
        dvlc.AppendTextColumn('id', width=40)
        dvlc.AppendTextColumn('artist', width=170)
        dvlc.AppendTextColumn('title', width=260)
        dvlc.AppendTextColumn('genre', width=80)
        for itemvalues in musicdata:
            dvlc.AppendItem(itemvalues)
            print itemvalues
        sizer = wx.BoxSizer()
        sizer.Add(dvlc, 1, wx.EXPAND)
        p.SetSizer(sizer)
        f.Show()
        return True

app = MiApp()
app.MainLoop()
