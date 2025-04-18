# -*- coding: utf-8 -*-

import os;
import pandas;
import glob;
import random;
from os import path;
from datetime import datetime;
from collections import Counter;

from classes.bcolors import bcolors;
from classes.utilities import utilities;
from classes.chart import chart;

# Consts

SEPARATOR       = "════════════════════════════════════";
LOTTO_NAME      = bcolors.output("E", bcolors.BOLD) + bcolors.output("x", bcolors.LIGHT_RED) + bcolors.output("tra", bcolors.BOLD);
SMALL_SEPARATOR = "────────────────────────────────────";
SINCE_DATE = "August 24th 1988";
NO1 = "NUMBER DRAWN 1";
NO2 = "NUMBER DRAWN 2";
NO3 = "NUMBER DRAWN 3";
NO4 = "NUMBER DRAWN 4";

# Global vars

utilities.DEBUG = False;
localPath = "./tmp/";
zipFileName = "Extra.zip";
oriCsvFileName = "Extra.csv";
csvFileName = "extra_" + datetime.now().strftime("%Y-%m-%d") + ".csv";
url = "http://www.bclc.com/DownloadableNumbers/CSV/" + zipFileName;


# Calculations

def getAllRowsCombinedData(csv):
    combinedData = csv[NO1].append(csv[NO2]).append(csv[NO3]).append(csv[NO4]);
    return pandas.Series(combinedData).value_counts();

def getNumbersWithOverallMostOccurence(csv):
    row = getAllRowsCombinedData(csv);
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberByRow(row, 0);
    numbers["nbr2"] = getOccurenceNumberByRow(row, 1);
    numbers["nbr3"] = getOccurenceNumberByRow(row, 2);
    numbers["nbr4"] = getOccurenceNumberByRow(row, 3);
    return numbers;

def getNumbersByPositionWithMostOccurence(csv):
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberBySerie(csv[NO1]);
    numbers["nbr2"] = getOccurenceNumberBySerie(csv[NO2]);
    numbers["nbr3"] = getOccurenceNumberBySerie(csv[NO3]);
    numbers["nbr4"] = getOccurenceNumberBySerie(csv[NO4]);
    return numbers;

def getNumbersWithOverallLeastOccurence(csv):
    row = getAllRowsCombinedData(csv);
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberByRow(row, -1);
    numbers["nbr2"] = getOccurenceNumberByRow(row, -2);
    numbers["nbr3"] = getOccurenceNumberByRow(row, -3);
    numbers["nbr4"] = getOccurenceNumberByRow(row, -4);
    return numbers;

def getNumbersByPositionWithLeastOccurence(csv):
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberBySerie(csv[NO1], -1);
    numbers["nbr2"] = getOccurenceNumberBySerie(csv[NO2], -1);
    numbers["nbr3"] = getOccurenceNumberBySerie(csv[NO3], -1);
    numbers["nbr4"] = getOccurenceNumberBySerie(csv[NO4], -1);
    return numbers;

def getAllNumbersSortedByOccurence(csv): # Graph
    row = getAllRowsCombinedData(csv);
    numbers = {};
    for i in range(len(row)):
        numbers.update({"nbr" + str(i): getOccurenceNumberByRow(row, i)});
    return numbers;

def getOccurenceNumberBySerie(serie, index = 0):
    row = pandas.Series(serie).value_counts();
    return getOccurenceNumberByRow(row, index);

def getOccurenceNumberByRow(row, index = 0):
    number = list(row.keys())[index];
    occurences = row.iloc[index];
    return {"number": number, "occurences": occurences};

# Output

def outputReport(title, numbers, showOccurences = True):
    print(SEPARATOR);
    print(title);
    print(SEPARATOR);
    outputReportList(numbers);
    if showOccurences:
        print(SMALL_SEPARATOR);
        print("Occurences");
        outputReportList(numbers, showOccurences);
    print(SEPARATOR);

def outputReportList(numbers, showOccurences = False):
    result = "";
    lastIndex = list(numbers)[-1];
    for key, entry in numbers.items():
        number = bcolors.output(entry["number"], bcolors.LIGHT_GREEN);
        occurences = str(entry["occurences"]);
        if key != lastIndex:
            result += "{} - ".format(number) if not showOccurences else "{} {}× - ".format(number, occurences);
        else:
            result += "{}".format(number) if not showOccurences else "{} {}×".format(number, occurences);
    print(result);


# Main

def getUpToDateCsvFile():
    if not path.exists(localPath): os.mkdir(localPath);
    if not path.exists(localPath + csvFileName):
        utilities.downloadUrl(url, localPath + zipFileName);
        utilities.extractZip(localPath + zipFileName, localPath);
        if path.exists(localPath + oriCsvFileName):
            # Rename file to today's date
            os.replace(localPath + oriCsvFileName, localPath + csvFileName);
    else:
        utilities.log("CSV file already up to date.");
    cleanup();

def cleanup():
    utilities.log("Cleanup temp files.");
    # Delete zip file
    if path.exists(localPath + zipFileName):
        os.remove(localPath + zipFileName);
    # Delete old csv but keep today's file, so that we don't download it again unnecessarily.
    for CleanUp in glob.glob(localPath + "extra_*.csv"):
        if not CleanUp.endswith(csvFileName):
            os.remove(CleanUp);

def showMenuOptions():
    print("""Actions:
# Hot numbers
-1 Get a forecast with the most reccuring numbers overall.
-2 Get a forecast with the most reccuring numbers by position.
# Cold numbers
-3 Get a forecast with the least reccuring numbers overall.
-4 Get a forecast with the least reccuring numbers by position.
# Graph
-5 Get a graph of all Extra numbers occurences since {} (ordered by number).
-6 Get a graph of all Extra numbers occurences since {} (ordered by occurences).
-graph|g Generate all graphs and save them as png.
# Misc
-help|h Help menu.
-quit|q Quit application.""".format(SINCE_DATE, SINCE_DATE));
    print(SEPARATOR);

def main():
    getUpToDateCsvFile();
    csv = utilities.readCsvFile(localPath + csvFileName);
    if csv is None:
        print("Invalid CSV closing now.");
        return;

    print(SEPARATOR);
    print("Lotto " + LOTTO_NAME + " draw forecast " + datetime.now().strftime("%Y-%m-%d"));
    print("Based on all drawings since {}.".format(SINCE_DATE));
    print(SEPARATOR);
    showMenuOptions();
    quitApp = False;
    while not quitApp:
        action = str(input("Enter your desired action: ")).lower();
        if action == "1":
            data = getNumbersWithOverallMostOccurence(csv);
            outputReport("Most reccuring numbers overall forecast", data);
        elif action == "2":
            data = getNumbersByPositionWithMostOccurence(csv);
            outputReport("Most reccuring numbers by position forecast", data);
        elif action == "3":
            data = getNumbersWithOverallLeastOccurence(csv);
            outputReport("Least reccuring numbers overall forecast", data);
        elif action == "4":
            data = getNumbersByPositionWithLeastOccurence(csv);
            outputReport("Least reccuring numbers by position forecast", data);
        elif action == "5":
            data = getAllNumbersSortedByOccurence(csv);
            plt = chart.generateGraph(
                "All lotto Extra numbers occurences since {} (ordered by number)".format(SINCE_DATE), data, chart.modeNumber, 20
            );
            plt.show();
        elif action == "6":
            data = getAllNumbersSortedByOccurence(csv);
            plt = chart.generateGraph(
                "All lotto Extra numbers occurences since {} (ordered by occurences)".format(SINCE_DATE), data, chart.modeOccurences, 20
            );
            plt.show();
        elif action == "graph" or action == "g":
            data = getAllNumbersSortedByOccurence(csv);
            plt = chart.generateGraph(
                "All lotto Extra numbers occurences since {} (ordered by number)".format(SINCE_DATE), data, chart.modeNumber, 20
            );
            chart.saveGraph(plt, "Extra numbers occurences (ordered by number)");
            plt = chart.generateGraph(
                "All lotto Extra numbers occurences since {} (ordered by occurences)".format(SINCE_DATE), data, chart.modeOccurences, 20
            );
            chart.saveGraph(plt, "Extra numbers occurences (ordered by occurences)");
        elif action == "help" or action == "h":  
            showMenuOptions();
        elif action == "quit" or action == "q":
            quitApp = True;
        else:
            print("Invalid action. Please choose a valid action.");
            showMenuOptions();

if __name__ == "__main__":
   main();
