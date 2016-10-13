#!/root/anaconda2/bin/python
import sys
import os

import pygal

def filetodata(_file):
    fosplit = _file.read().split('\n')

    chart = pygal.Line()
    chart.title = 'Example'

    x = []
    y = []

    for eachline in fosplit:
        line = eachline.split(',')

        if str(eachline) is str(fosplit[0]):
            if str(eachline) != "":
                try:
                    int(line[0])
                    int(line[1])
                except(ValueError):
                    try:
                        str(line[0])
                        str(line[1])
                        #plt.xlabel(line[0])
                        #plt.ylabel(line[1])
                        chart._x_title(line[0])
                        chart._y_title(line[1])
                    except:
                        ####print "Oops! Invalid first line (int or str)"
                        #quit()
                        pass

        if eachline is not fosplit[0]:
            try:
                if line[0]:
                    if line[1]:
                        if int(line[0]) and int(line[1]):
                            x.append(int(line[0]))
                            y.append(int(line[1]))
                        else:
                            ####print "One or more values were not integers"
                            #quit()
                            pass
            except IndexError:
                ####print "Oops! Invalid data"
                #quit()
                pass

    ####print "current file: %s" %file_path

    #print x
    #print y

    #plt.plot(x,y)
    #plt.show()

    chart.x_labels = range(0,len(x))
    chart.add("hello", y)

    chart_data = chart.render_data_uri()

    return chart_data
