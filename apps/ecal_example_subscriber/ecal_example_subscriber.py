# Copyright (c) 2024 Elektrobit Automotive GmbH and others

# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# SPDX-License-Identifier: Apache-2.0

import sys, time, logging

import ecal.core.core as ecal_core
from ecal.core.subscriber import StringSubscriber

logger = logging.getLogger("ecal_example_subscriber")
stdout = logging.StreamHandler(stream=sys.stdout)
stdout.setLevel(logging.INFO)
logger.addHandler(stdout)
logger.setLevel(logging.INFO)

# Callback for receiving messages
def callback(topic_name, msg, time):
    try:
        logger.info(f"Received: {msg}")
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    logger.info("Starting ecal example subscriber app...")

    # Initialize eCAL
    ecal_core.initialize(sys.argv, "eCAL Example Subscriber app")

    # Create a subscriber that listens to the "hello_topic" eCAL topic
    sub = StringSubscriber("hello_topic")

    # Set the Callback
    sub.set_callback(callback)
    
    # Just don't exit
    while ecal_core.ok():
        time.sleep(0.5)
    
    # finalize eCAL API
    ecal_core.finalize()