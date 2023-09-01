import os

with open("robocop_output.txt", "r") as input_file:
    input_content = input_file.read()

sections = input_content.split("\n" + "-" * 50 + "\n")

html_content = '<html><body> <h1>RoboCop Tests Log</h1>'
total_scan_time = 0
for section in sections:
    lines = section.strip().split("\n")
    if lines:
        table_content = (
            "<table class='statistics'><tr>"
            "<th>Folder</th>"
            "<th>Line</th>"
            "<th>[W] Code</th>"
            "<th>Issue</th></tr>"
        )
        

        for line in lines:

            if line.find(".robot") != -1:
                folder_line_parts = line.split(".robot:")
                information = folder_line_parts[1].split(" ")
                error_line = information[0]
                error_information = information[1] + " " + information[2]
                error_description = ""
                error_description = " ".join(information[3:]) 
                table_content += (
                    f"<tr><td>{folder_line_parts[0]}.robot</td>"
                    f"<td>{error_line}</td>"
                    f"<td>{error_information}</td>"
                    f"<td>{error_description}</td></tr>"
                )
                
            TestCaseName = folder_line_parts[0].split(os.getcwd())
            if line.find("Reported:") != -1:
                table_content += "</table>"
                html_content += f"<h2>TC{TestCaseName[1]}</h2>"
                html_content += table_content
                reported_reformat = line.split(" ")
                currentDate = " ".join(reported_reformat[1:]) 
                html_content += f"<p><strong>{reported_reformat[0]}</strong> {currentDate}</p>"
                
                
            if line.find("Found") != -1: 
                found_warnings = line.split(":")    
                html_content += f"<p>{found_warnings[0]}"
                state = found_warnings[1].split(",")
                for s in state:
                    parts = s.strip().split()  # Split the string into words
                    count = parts[0]  # The first part is the count
                    type_ = parts[1]
                    if type_ == "WARNINGs" or type_ == "WARNINGs.":
                        html_content += f" <span class='warning'>{count} {type_}</span> "
                    if type_ == "INFOs" or type_ == "INFOs.":
                        html_content += f" <span class='info'>{count} {type_}</span> "

                html_content += "</p>"
                    
            if line.find("Scan finished") != -1: 
                scan_info = line.split(' ')
                scan_time = scan_info[3].replace('s.','') 
                print(scan_time)    
                total_scan_time += float(scan_time)
                html_content += f"<p>Scan finished in <span style='color:green'>{scan_info[3]}</span></p>"

            if line.find("--------") != -1:
                table_content = (
                    "<table class='statistics'><tr>"
                    "<th>Folder</th>"
                    "<th>Line</th>"
                    "<th>[W] Code</th>"
                    "<th>Issue</th></tr>"
                )
html_content += f"Total Scan Time {round(total_scan_time,3)}s"
html_content += "<p>Issues by ID:<p>"\
    "<p>W0508 (line-too-long) : 4 </p>"\
    "<p>W1001 (trailing-whitespace) : 2 </p>"\
    "<p>W0302 (wrong-case-in-keyword-name) : 2 </p>"\
    "<p>W0203 (missing-doc-suite) : 1 </p>"\
    "<p>W1003 (empty-lines-between-sections) : 1 </p>"

html_content += "</body><style>.statistics{width: 65em;" \
    "border-collapse: collapse;" \
    "empty-cells: show;" \
    "margin-bottom: 1em;" \
    "display: table;" \
    "border-collapse: separate;" \
    "box-sizing: border-box;" \
    "text-indent: initial;" \
    "border-spacing: 2px;" \
    "border-color: gray;}" \
    ".statistics th {" \
    "background-color: #ddd;" \
    "padding: 0.2em 0.3em;" \
    "}" \
    ".statistics th, .statistics td {" \
    "border: 1px solid #ccc;" \
    "padding: 0.1em 0.3em;" \
    "}" \
    ".warning{background-color: #FFFF00;" \
    "color: #000 !important;" \
    "padding: 2px 5px;" \
    "font-size: 0.75em;" \
    "letter-spacing: 1px;" \
    "white-space: nowrap;" \
    "border: 1px solid black;" \
    "border-radius: 3px !important;}" \
    ".info{border: 1px solid black;" \
    "color: #000 !important;" \
    "padding: 2px 5px;" \
    "font-size: 0.75em;" \
    "letter-spacing: 1px;" \
    "white-space: nowrap;" \
    "border-radius: 3px !important;}" \
    "</style>" \
    "</html>"

# Write the HTML content to the output file
with open("robocop_output.html", "w") as output_file:
    output_file.write(html_content)

print("Conversion completed. Output saved to robocop_output.html.")
