def to_table(data, header=False, index=False):
    full_html = "<table>"
    header_html = "<thead><tr>"
    if header ==True:
        for i in data[0]:
            header_html+="<th>%s</th>"%str(i)
        header_html+="</tr></thead>"
        full_html+=header_html
        full_html+="<tbody>"
        for i in data[1:]:
            full_html+="<tr>"
            for j in i:
                full_html+="<td>%s</td>"%str(j)
        full_html+="</tr></tbody>"
    else:
        full_html+="<tbody>"
        for i in data[0:]:
            full_html+="<tr>"
            for j in i:
                full_html+="<td>%s</td>"%str(j)
        full_html+="</tr></tbody>"           
    full_html+="</table>"
    return full_html


if __name__=='__main__':
	print(to_table([["lorem", "ipsum"], ["dolor", "sit amet"]], True, True))