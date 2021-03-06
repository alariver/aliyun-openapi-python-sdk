# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class BindTagRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2016-08-01', 'BindTag')

	def get_TagName(self):
		return self.get_query_params().get('TagName')

	def set_TagName(self,TagName):
		self.add_query_param('TagName',TagName)

	def get_ClientKey(self):
		return self.get_query_params().get('ClientKey')

	def set_ClientKey(self,ClientKey):
		self.add_query_param('ClientKey',ClientKey)

	def get_AppKey(self):
		return self.get_query_params().get('AppKey')

	def set_AppKey(self,AppKey):
		self.add_query_param('AppKey',AppKey)

	def get_KeyType(self):
		return self.get_query_params().get('KeyType')

	def set_KeyType(self,KeyType):
		self.add_query_param('KeyType',KeyType)