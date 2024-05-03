res = [r"\begin{table}[!htb]",
       r"    \caption{这是标题}", 
       r"    \begin{tblr}{",
    ]

col_len = int(input("几列？"))
row_len = int(input("几行？"))

colspec = "        colspec={" + (col_len * "X[c,3]") + "},"

res.append(colspec)

def cell_con2_num(cell):
    return ord(cell[0]) - ord('A') + 1, int(cell[1:])

while True:
    need_merge = input("要合并单元格吗？Y/y-是，其他-不是：")
    if need_merge == "Y" or need_merge == "y":
        up = input("等待合并的单元格范围，左上角是？例如A2：")
        low = input("等待合并的单元格范围，右下角是？例如B4：")

        up_col, up_row = cell_con2_num(up)
        low_col, low_row = cell_con2_num(low)

        merge = "        cell{" + str(up_row) +"}{"+ str(up_col) +"}={r="+str(low_row-up_row+1)+",c="+str(low_col-up_col+1)+"}{c},"
        res.append(merge)
    else:
        break

res.append(r"    }")
simple_line = "       " + " & " * (col_len - 1)+ r" 1\\"
head_line = "       " + " 1 &" * (col_len - 1) + r" 1\\"
res.append(r"      \toprule")
res.append(head_line)
res.append(r"      \midrule")
for _ in range(row_len - 1):
    res.append(simple_line)
res.append(r"      \bottomrule")
res.append(r"    \end{tblr}")
res.append(r"\end{table}")


print("\n".join(res))

