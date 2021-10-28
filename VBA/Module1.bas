Attribute VB_Name = "Module1"

Function getSheets(filePath As String)
    
    Dim str As String
    Dim extension As String
    
    Set objFileSys = CreateObject("Scripting.FileSystemObject")
    extension = LCase(objFileSys.GetExtensionName(filePath))
    
    If extension = "xls" Or extension = "xlsx" Then
        '�ʃu�b�N���J��
        Workbooks.Open fileName:=filePath
        
        Set otherWb = Workbooks(Dir(filePath)) '�ʃu�b�N
            
        For i = 1 To otherWb.Sheets.Count
            str = str & otherWb.Sheets(i).Name
            
            If i + 1 <= otherWb.Sheets.Count Then
                If otherWb.Sheets(i + 1).Name <> "" Then
                    str = str & vbCrLf
                End If
            End If
        Next i
        
        otherWb.Close '�ʃu�b�N�����
    End If
    
    getSheets = str
End Function

Sub writeSheets()
    Dim row As Integer
    row = 1
    Do Until Cells(row, 1).Value = ""
        ActiveSheet.Cells(row, 3).Value = getSheets(ActiveSheet.Cells(row, 1))
        row = row + 1
    Loop
End Sub

