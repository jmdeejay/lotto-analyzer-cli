import os;
from os import path;
import matplotlib.pyplot as plt;
from matplotlib.widgets import Button;
import mplcursors;
import numpy as np;

graphPath = "./graphs/";

class chart:
	modeNumber = "number";
	modeOccurences = "occurences";
	orderMode = modeNumber;

	def generateGraph(title, values, order = modeNumber, width = 12, height = 5):
		flattenedValues = chart.flattenValues(values);
		sortedValues = chart.sortValues(flattenedValues, order);
		numbers = chart.getNumber(sortedValues);
		occurences = chart.getOccurences(sortedValues);

		x = np.arange(len(numbers));
		fig, ax = plt.subplots();
		fig.set_size_inches(width, height, forward = True);
		fig.canvas.set_window_title(title);
		fig.set_tight_layout(True);

		minYBoundary = max(min(occurences) - 100, 0);
		maxYBoundary = max(occurences) + 50;
		ax.set_ylim(minYBoundary, maxYBoundary);

		plt.title(title);
		plt.margins(x = 0.01, y = 0.3, tight = True);
		plt.xlabel("Lotto numbers");
		plt.ylabel("Occurences");
		plt.xticks(x, numbers);
		bars = plt.bar(x, occurences);

		"""
		# Reorder button
		reorderBtnAx = plt.axes([0.66, 0.01, 0.24, 0.05]); # [left, top, width, height]
		reorderBtn = Button(reorderBtnAx, 'Reorder by (lotto number | occurences)');
		reorderBtn.on_clicked(lambda event: chart.reorder(event));
		"""

		# chart.autoLabel(ax, bars);
		crs = mplcursors.cursor(ax, hover = True);
		crs.connect("add", lambda sel: sel.annotation.set_text(
			str(numbers[sel.target.index]) + ": " + str(occurences[sel.target.index]) + " occurences"
		));
		return plt;

	def saveGraph(plt, filename):
		if not path.exists(graphPath): os.mkdir(graphPath);
		plt.savefig(graphPath + filename + ".png");


	# Data

	def flattenValues(values):
		result = {};
		for entry in values.values():
			result.update({entry["number"]: entry["occurences"]});
		return result;

	def sortValues(flattenedValues, order = modeNumber):
		if order == chart.modeNumber:
			return sorted(flattenedValues.items(), key = lambda x: x[0], reverse = False);
		else:
			return sorted(flattenedValues.items(), key = lambda x: x[1], reverse = True);

	def getNumber(flattenedValues):
		result = [];
		for entry in flattenedValues:
			result.append(entry[0]);
		return result;

	def getOccurences(flattenedValues):
		result = [];
		for entry in flattenedValues:
			result.append(entry[1]);
		return result;


	# Graph utilities

	def reorder(event):
		if chart.orderMode == chart.modeNumber:
			chart.orderMode = chart.modeOccurences;
		else:
			chart.orderMode = chart.modeNumber;
		print("order = " + chart.orderMode);

	def autoLabel(ax, rects):
	    for rect in rects:
	        height = rect.get_height();
	        ax.annotate('{}'.format(height),
	            xy = (rect.get_x() + rect.get_width() / 2, height),
	            xytext = (0, 3),
	            textcoords = "offset points",
	            ha = 'center', va = 'bottom'
	        );
