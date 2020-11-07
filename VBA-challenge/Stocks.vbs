Attribute VB_Name = "Module1"
Sub stocks()

'declaring variables
Dim ticker As String
Dim t As Long
Dim s As Long
Dim total As Double
Dim open_px As Double
Dim close_px As Double
Dim rowcount1 As Long
'Dim rowcount2 As Long
Dim yr_chg As Double
Dim per_chg As Double
Dim i As Integer
Dim wksht As Worksheet
Dim max_per As Double
Dim min_per As Double
Dim max_vol As Double

'looping through worksheets
For i = 1 To ActiveWorkbook.Worksheets.Count
Worksheets(i).Activate

'assigning header titles
Range("i1").Value = "Ticker"
Range("j1").Value = "Yearly Change"
Range("k1").Value = "Percentage Change"
Range("l1").Value = "Total Volume"

Range("o2").Value = "Greatest % Increase"
Range("o3").Value = "Greatest % Decrease"
Range("o4").Value = "Greatest Total Volume"

Range("p1").Value = "Ticker"
Range("q1").Value = "Value"

'determining final row of table
rowcount1 = Cells(Rows.Count, "A").End(xlUp).Row

s = 2
total = 0
open_px = Range("c2").Value
close_px = 0

'iterating through rows to determine values
For t = 2 To rowcount1

If Cells(t, 1).Value <> Cells(t + 1, 1).Value Then

close_px = Cells(t, 6).Value
yr_chg = close_px - open_px
total = total + Cells(t, 7).Value
    If open_px > 0 Then
    per_chg = yr_chg / open_px
    
    End If

'set the values to the new table

Range("i" & s).Value = Range("a" & t).Value
Range("j" & s).Value = yr_chg
Range("k" & s).Value = per_chg
Range("l" & s).Value = total

'resetting shared variables
total = 0
s = s + 1
open_px = Cells(t + 1, 3).Value

Else
total = total + Range("g" & t).Value


End If
Next t

rowcount2 = Cells(Rows.Count, "I").End(xlUp).Row
'assigning formats
For s = 2 To rowcount2
If Range("j" & s).Value < 0 Then
Range("j" & s).Interior.ColorIndex = 3
Else
Range("j" & s).Interior.ColorIndex = 4

End If
Range("k" & s).NumberFormat = "0.00%"

max_per = Application.WorksheetFunction.Max(Range("k:k"))
min_per = Application.WorksheetFunction.Min(Range("k:k"))
max_vol = Application.WorksheetFunction.Max(Range("l:l"))


'assigning greatest % increase and decrease
If Range("k" & s).Value = max_per Then
Range("p2").Value = Range("i" & s).Value
Range("q2").Value = Range("k" & s).Value
ElseIf Range("k" & s).Value = min_per Then
Range("p3").Value = Range("i" & s).Value
Range("q3").Value = Range("k" & s).Value
End If
Range("q2").NumberFormat = "0.00%"
Range("q3").NumberFormat = "0.00%"

'assigning greatest total volume
If Range("l" & s).Value = max_vol Then
Range("q4").Value = Range("l" & s).Value
End If

Next s

Next i


End Sub
