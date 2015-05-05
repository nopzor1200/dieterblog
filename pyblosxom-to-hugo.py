#!/usr/bin/env python3

# note this script is not super clean or failsafe.
# but it works for me

py="."
hugo="hugotest"
import glob
import re
import pathlib
import html

def fixheader(lines):
    date = ""
    time = ""
    guid = ""
    tags = []

    for i, line in enumerate(lines):
        line = line.strip()
        if i == 0:
            # replace entity refs like &amp; to &
            # if title contains ", those should be escaped for hugo
            title = html.unescape(line.replace('"', '\\\"'))
        else:
            if "pubdate " in line:
                date = re.sub(".*pubdate *", "", line)
            elif "pubtime " in line:
                time = re.sub(".*pubtime *", "", line)
            elif "tags " in line:
                tags = re.sub(".*tags *", "", line).split(",")
            elif "guid " in line:
                guid = re.sub(".*guid *", "", line)
            elif line.startswith("#"):
                raise Exception("unknown header directive: %s", line)
            elif line == "":
                # ignore empty line
                pass
            else:
                break

    if not date or not time:
        raise Exception("incomplete header")

    newheader = [
        "+++",
        "title = \"%s\"" % title,
        "date = \"%sT%s-04:00\"" % (date, time),
        "tags = [%s]" % ', '.join(['"%s"' % i for i in tags]),
        "+++"
    ]

    lines = newheader + lines[i+1:]
    return lines

def fixreadmore(lines):
    return map(lambda line: line.replace("<!--break-->", "<!--more-->"), lines)

# note, not robust. e.g. will fail if you have </code> in your code block
def fixhighlight(lines):
    out = []
    for i, line in enumerate(lines):
        # quote lang arg because lang can be like html+php
        line = re.sub('<code lang="([a-zA-Z\+]+)">', '{{< highlight "\\1" "style=default" >}}', line)
        line = line.replace('<code>', '{{< highlight "c" "style=default" >}}')  # sorry i really don't think we can do better than this, pygments invoked via hugo needs a lang specified
        out.append(line.replace('</code>', '{{< /highlight >}}'))
    return out
  


entries = glob.glob('entries/*')
for entry in entries:
    base = entry[8:]
    draft = False  # we actually ignore this cause i don't have drafts like this
    if base[-4:] == ".txt":
        new = hugo + "/content/post/" +base[:-4] + ".md"
    elif ".txt" in base:  # .txt.draft, .txt.unpub, etc
        draft = True
        new = hugo + "/content/post/" + re.sub("\.txt.*", ".md", base)
    else:  # .draft, .unpub
        draft = True
        p = pathlib.PurePath(entry)
        new = hugo + "/content/post/" + p.with_suffix('.md').name

    print(base, "---->", new)
    f = open(entry, "r")
    lines = f.readlines()
    lines = fixhighlight(fixreadmore(fixheader(lines)))
    f.close()
    f = open(new, "w")
    f.write("\n".join(lines))
    f.close()

pages = glob.glob('pages/*')
for page in pages:
    base = page[6:]
    # for my case we can assume .txt extension
    new = hugo + "/content/" +base[:-4] + ".md"
    print(base, "---->", new)
    f = open(page, "r")
    lines = f.readlines()
    lines = fixheader(lines)
    f.close()
    f = open(new, "w")
    f.write("\n".join(lines))
    f.close()






        
