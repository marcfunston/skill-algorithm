# Copyright 2017, Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# author Marc Funston
# date 4/09/2018


from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from random import choice

class AlgorithmSkill(MycroftSkill):
    def __init__(self):
        super(AlgorithmSkill, self).__init__(name="AlgorithmSkill")

    @intent_handler(IntentBuilder("MergeSortIntent").require("Algorithm").require("MergeSort"))
    def handle_merge_sort_best_intent(self, message):
        self.speak_dialog("merge.sort")

    @intent_handler(IntentBuilder("CountingSortIntent").require("Algorithm").require("CountingSort"))
    def handle_counting_sort_intent(self, message):
        self.speak_dialog("counting.sort")

    @intent_handler(IntentBuilder("LinearSortIntent").require("Algorithm").require("LinearSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("linear.sort")

    @intent_handler(IntentBuilder("HeapSortIntent").require("Algorithm").require("HeapSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("heap.sort")

    @intent_handler(IntentBuilder("QuickSortIntent").require("Algorithm").require("QuickSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("quick.sort")

    @intent_handler(IntentBuilder("RadixSortIntent").require("Algorithm").require("RadixSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("radix.sort")

    @intent_handler(IntentBuilder("TimSortIntent").require("Algorithm").require("TimSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("tim.sort")

    @intent_handler(IntentBuilder("BubbleSortIntent").require("Algorithm").require("BubbleSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("bubble.sort")

    @intent_handler(IntentBuilder("SelectionSortIntent").require("Algorithm").require("SelectionSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("selection.sort")

    @intent_handler(IntentBuilder("TreeSortIntent").require("Algorithm").require("TreeSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("tree.sort")

    @intent_handler(IntentBuilder("BucketSortIntent").require("Algorithm").require("BucketSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("bucket.sort")

    @intent_handler(IntentBuilder("ShellSortIntent").require("Algorithm").require("ShellSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("shell.sort")

    @intent_handler(IntentBuilder("CubeSortIntent").require("Algorithm").require("CubeSort"))
    def handle_linear_sort_intent(self, message):
        self.speak_dialog("cube.sort")

    def stop(self):
        pass

def create_skill():
    return AlgorithmSkill()
