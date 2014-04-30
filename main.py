#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import other_funcs

form="""
<form method="post">
    What is your birthday?
    <br>
    <label> Month
        <input type="text" name="month">
    </label>
    <label> Day
        <input type="text" name="day">
    </label>
    <label> Year
        <input type="text" name="year">
    </label>
    <br>
    <br>
	<input type = "submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)


    def post(self):
        #other_funcs.valid_month(month)
        #other_funcs.valid_day(day)
        #other_funcs.valid_year(year)

        user_month = other_funcs.valid_month(self.request.get('month'))
        user_day = other_funcs.valid_day(self.request.get('day'))
        user_year = other_funcs.valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.response.out.write(form)
        else:
            self.response.out.write("Thanks! That's a valid day!")




app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
