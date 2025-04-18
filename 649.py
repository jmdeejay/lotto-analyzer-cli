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

VERSION = "1.2";
SEPARATOR       = "════════════════════════════════════";
LOTTO_NAME      = bcolors.output("6", bcolors.LIGHT_RED) + bcolors.output("/", bcolors.BOLD) + bcolors.output("49", bcolors.LIGHT_BLUE);
SMALL_SEPARATOR = "────────────────────────────────────";
SINCE_DATE = "June 12th 1982";
NO1 = "NUMBER DRAWN 1";
NO2 = "NUMBER DRAWN 2";
NO3 = "NUMBER DRAWN 3";
NO4 = "NUMBER DRAWN 4";
NO5 = "NUMBER DRAWN 5";
NO6 = "NUMBER DRAWN 6";
NO_EXTRA = "BONUS NUMBER";

# Global vars

utilities.DEBUG = False;
localPath = "./tmp/";
zipFileName = "649.zip";
oriCsvFileName = "649.csv";
csvFileName = "649_" + datetime.now().strftime("%Y-%m-%d") + ".csv";
url = "http://www.bclc.com/DownloadableNumbers/CSV/" + zipFileName;


# Calculations

def getAllRowsCombinedData(csv, withBonus = True):
    combinedData = csv[NO1].append(csv[NO2]).append(csv[NO3]).append(csv[NO4]).append(csv[NO5]).append(csv[NO6]);
    if withBonus == True:
        combinedData = combinedData.append(csv[NO_EXTRA]);
    return pandas.Series(combinedData).value_counts();

def getRandomTopMostReccuringNumbers(csv):
    row = getAllRowsCombinedData(csv);
    randomIndex = random.sample(range(0, 11), 6);
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberByRow(row, randomIndex[0]);
    numbers["nbr2"] = getOccurenceNumberByRow(row, randomIndex[1]);
    numbers["nbr3"] = getOccurenceNumberByRow(row, randomIndex[2]);
    numbers["nbr4"] = getOccurenceNumberByRow(row, randomIndex[3]);
    numbers["nbr5"] = getOccurenceNumberByRow(row, randomIndex[4]);
    numbers["nbr6"] = getOccurenceNumberByRow(row, randomIndex[5]);
    return numbers;

def getNumbersWithOverallMostOccurence(csv):
    row = getAllRowsCombinedData(csv);
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberByRow(row, 0);
    numbers["nbr2"] = getOccurenceNumberByRow(row, 1);
    numbers["nbr3"] = getOccurenceNumberByRow(row, 2);
    numbers["nbr4"] = getOccurenceNumberByRow(row, 3);
    numbers["nbr5"] = getOccurenceNumberByRow(row, 4);
    numbers["nbr6"] = getOccurenceNumberByRow(row, 5);
    return numbers;

def getNumbersByPositionWithMostOccurence(csv):
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberBySerie(csv[NO1]);
    numbers["nbr2"] = getOccurenceNumberBySerie(csv[NO2]);
    numbers["nbr3"] = getOccurenceNumberBySerie(csv[NO3]);
    numbers["nbr4"] = getOccurenceNumberBySerie(csv[NO4]);
    numbers["nbr5"] = getOccurenceNumberBySerie(csv[NO5]);
    numbers["nbr6"] = getOccurenceNumberBySerie(csv[NO6]);
    numbers["nbrExtra"] = getOccurenceNumberBySerie(csv[NO_EXTRA]);
    return numbers;

def getRandomLeastReccuringNumbers(csv):
    row = getAllRowsCombinedData(csv);
    randomIndex = random.sample(range(len(row)-12, len(row)), 6);
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberByRow(row, randomIndex[0]);
    numbers["nbr2"] = getOccurenceNumberByRow(row, randomIndex[1]);
    numbers["nbr3"] = getOccurenceNumberByRow(row, randomIndex[2]);
    numbers["nbr4"] = getOccurenceNumberByRow(row, randomIndex[3]);
    numbers["nbr5"] = getOccurenceNumberByRow(row, randomIndex[4]);
    numbers["nbr6"] = getOccurenceNumberByRow(row, randomIndex[5]);
    return numbers;

def getNumbersWithOverallLeastOccurence(csv):
    row = getAllRowsCombinedData(csv);
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberByRow(row, -1);
    numbers["nbr2"] = getOccurenceNumberByRow(row, -2);
    numbers["nbr3"] = getOccurenceNumberByRow(row, -3);
    numbers["nbr4"] = getOccurenceNumberByRow(row, -4);
    numbers["nbr5"] = getOccurenceNumberByRow(row, -5);
    numbers["nbr6"] = getOccurenceNumberByRow(row, -6);
    return numbers;

def getNumbersByPositionWithLeastOccurence(csv):
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberBySerie(csv[NO1], -1);
    numbers["nbr2"] = getOccurenceNumberBySerie(csv[NO2], -1);
    numbers["nbr3"] = getOccurenceNumberBySerie(csv[NO3], -1);
    numbers["nbr4"] = getOccurenceNumberBySerie(csv[NO4], -1);
    numbers["nbr5"] = getOccurenceNumberBySerie(csv[NO5], -1);
    numbers["nbr6"] = getOccurenceNumberBySerie(csv[NO6], -1);
    numbers["nbrExtra"] = getOccurenceNumberBySerie(csv[NO_EXTRA], -1);
    return numbers;

def getRandomMidReccuringNumbers(csv):
    row = getAllRowsCombinedData(csv);
    randomIndex = random.sample(range(12, len(row)-12), 6);
    numbers = {};
    numbers["nbr1"] = getOccurenceNumberByRow(row, randomIndex[0]);
    numbers["nbr2"] = getOccurenceNumberByRow(row, randomIndex[1]);
    numbers["nbr3"] = getOccurenceNumberByRow(row, randomIndex[2]);
    numbers["nbr4"] = getOccurenceNumberByRow(row, randomIndex[3]);
    numbers["nbr5"] = getOccurenceNumberByRow(row, randomIndex[4]);
    numbers["nbr6"] = getOccurenceNumberByRow(row, randomIndex[5]);
    return numbers;

def getLottoRandomNumbers():
    randomNumber = random.sample(range(1, 49), 6);
    numbers = {};
    numbers["nbr1"] = {"number": randomNumber[0], "occurences": ""};
    numbers["nbr2"] = {"number": randomNumber[1], "occurences": ""};
    numbers["nbr3"] = {"number": randomNumber[2], "occurences": ""};
    numbers["nbr4"] = {"number": randomNumber[3], "occurences": ""};
    numbers["nbr5"] = {"number": randomNumber[4], "occurences": ""};
    numbers["nbr6"] = {"number": randomNumber[5], "occurences": ""};
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
            if lastIndex == "nbrExtra":
                result += "Bonus ({})".format(number) if not showOccurences else "Bonus ({} {}×)".format(number, occurences);
            else :
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
    # Delete old 649_*.csv but keep today's file, so that we don't download it again unnecessarily.
    for CleanUp in glob.glob(localPath + "649_*.csv"):
        if not CleanUp.endswith(csvFileName):
            os.remove(CleanUp);


"""
Additional ideas:
- Add with / without bonus number stats
- Per 60-day cycle
- Per draw: distribution of results (gaussian, linear, etc.)
- Sums of picked number
- Add possibility to filter results by date
"""

def showMenuOptions():
    print("""Actions:
# Hot numbers
-1 Get a forecast with random 12 top most reccuring numbers.
-2 Get a forecast with the most reccuring numbers overall.
-3 Get a forecast with the most reccuring numbers by position.
# Cold number
-4 Get a forecast with random 12 least reccuring numbers.
-5 Get a forecast with the least reccuring numbers overall.
-6 Get a forecast with the least reccuring numbers by position.
# Random
-7 Get a forecast with random 25 (neither hot|cold) reccuring numbers.
-8 Get a forecast with random numbers.
# Graph
-9 Get a graph of all 6/49 numbers occurences since {} (ordered by number).
-10 Get a graph of all 6/49 numbers occurences since {} (ordered by occurences).
-graph|g Generate all graphs and save them as png.
# Misc
-help|h Help menu.
-version|v Application version.
-quit|q Quit application.""".format(SINCE_DATE, SINCE_DATE));
    print(SEPARATOR);

def main():
    getUpToDateCsvFile();
    csv = utilities.readCsvFile(localPath + csvFileName);
    if csv is None:
        print("Invalid CSV closing now.");
        return;

    print(SEPARATOR);
    print("Lotto " + LOTTO_NAME + " v" + VERSION + " draw forecast " + datetime.now().strftime("%Y-%m-%d"));
    print("Based on all drawings since {}.".format(SINCE_DATE));
    print(SEPARATOR);
    showMenuOptions();
    quitApp = False;
    while not quitApp:
        action = str(input("Enter your desired action: ")).lower();
        if action == "1":
            data = getRandomTopMostReccuringNumbers(csv);
            outputReport("Random 12 top most reccuring numbers forecast", data);
        elif action == "2":
            data = getNumbersWithOverallMostOccurence(csv);
            outputReport("Most reccuring numbers overall forecast", data);
        elif action == "3":
            data = getNumbersByPositionWithMostOccurence(csv);
            outputReport("Most reccuring numbers by position forecast", data);
        elif action == "4":
            data = getRandomLeastReccuringNumbers(csv);
            outputReport("Random 12 least reccuring numbers forecast", data);
        elif action == "5":
            data = getNumbersWithOverallLeastOccurence(csv);
            outputReport("Least reccuring numbers overall forecast", data);
        elif action == "6":
            data = getNumbersByPositionWithLeastOccurence(csv);
            outputReport("Least reccuring numbers by position forecast", data);
        elif action == "7":
            data = getRandomMidReccuringNumbers(csv);
            outputReport("Random 25 (neither hot|cold) reccuring numbers forecast", data);
        elif action == "8":
            data = getLottoRandomNumbers();
            outputReport("Random numbers forecast", data, False);
        elif action == "9":
            data = getAllNumbersSortedByOccurence(csv);
            plt = chart.generateGraph("All lotto 6/49 numbers occurences since {} (ordered by number)".format(SINCE_DATE), data, chart.modeNumber);
            plt.show();
        elif action == "10":
            data = getAllNumbersSortedByOccurence(csv);
            plt = chart.generateGraph("All lotto 6/49 numbers occurences since {} (ordered by occurences)".format(SINCE_DATE), data, chart.modeOccurences);
            plt.show();
        elif action == "graph" or action == "g":
            data = getAllNumbersSortedByOccurence(csv);
            plt = chart.generateGraph(
                "All lotto 6/49 numbers occurences since {} (ordered by number)".format(SINCE_DATE), data, chart.modeNumber
            );
            chart.saveGraph(plt, "649 numbers occurences (ordered by number)");
            plt = chart.generateGraph(
                "All lotto 6/49 numbers occurences since {} (ordered by occurences)".format(SINCE_DATE), data, chart.modeOccurences
            );
            chart.saveGraph(plt, "649 numbers occurences (ordered by occurences)");
        elif action == "help" or action == "h":  
            showMenuOptions();
        elif action == "version" or action == "v":  
            print("Lotto " + LOTTO_NAME + ": v" + VERSION);
        elif action == "quit" or action == "q":
            quitApp = True;
        else:
            print("Invalid action. Please choose a valid action.");
            showMenuOptions();

if __name__ == "__main__":
   main();
