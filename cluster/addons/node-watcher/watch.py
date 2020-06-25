#!/bin/env python

from kubernetes import client, config, watch

import os, json

if "KUBECONFIG" in os.environ:
    config.load_kube_config()
else:
    config.incluster_config.load_incluster_config()

core = client.CoreV1Api()

def add_node_label(name, key, val):
    body = dict(metadata=dict(labels=dict([(key, val)])))
    core.patch_node(name, body)


if __name__ == "__main__":
    # watch for node-related events
    print("Watching for events...")
    watch = watch.Watch()
    for event in watch.stream(core.list_node):
        event_type = event['type']
        # get node metadata
        node = event['object']
        name = node.metadata.name
        labels = node.metadata.labels
        role = ""

        if "node.kubernetes.io/master" in list(labels):

            # dictionary syntax = dict.get(key, default=None)
            role = labels.get('role', 'master')

            # we are only interested in create node events
            print("Event: {0} (name={1}, role={2})".format(event_type, name, role))
            if event_type != "ADDED":
                continue

            # add node-role.kubernetes.io label
            value = "{0}".format(role)
            add_node_label(name, "node-role.kubernetes.io/"+value, value)
        
        elif "node.kubernetes.io/worker" in list(labels):

            # dictionary syntax = dict.get(key, default=None)
            role = labels.get('role', 'worker')

            # we are only interested in create node events
            print("Event: {0} (name={1}, role={2})".format(event_type, name, role))
            if event_type != "ADDED":
                continue

            # add node-role.kubernetes.io label
            value = "{0}".format(role)
            add_node_label(name, "node-role.kubernetes.io/"+value, value)
        
        elif "node.kubernetes.io/twistlock" in list(labels):

            # dictionary syntax = dict.get(key, default=None)
            role = labels.get('role', 'twistlock')

            # we are only interested in create node events
            print("Event: {0} (name={1}, role={2})".format(event_type, name, role))
            if event_type != "ADDED":
                continue

            # add node-role.kubernetes.io label
            value = "{0}".format(role)
            add_node_label(name, "node-role.kubernetes.io/"+value, value)

        elif "node.kubernetes.io/jenkins" in list(labels):

            # dictionary syntax = dict.get(key, default=None)
            role = labels.get('role', 'jenkins')

            # we are only interested in create node events
            print("Event: {0} (name={1}, role={2})".format(event_type, name, role))
            if event_type != "ADDED":
                continue

            # add node-role.kubernetes.io label
            value = "{0}".format(role)
            add_node_label(name, "node-role.kubernetes.io/"+value, value)
        
        elif "node.kubernetes.io/infra" in list(labels):

            # dictionary syntax = dict.get(key, default=None)
            role = labels.get('role', 'infra')

            # we are only interested in create node events
            print("Event: {0} (name={1}, role={2})".format(event_type, name, role))
            if event_type != "ADDED":
                continue

            # add node-role.kubernetes.io label
            value = "{0}".format(role)
            add_node_label(name, "node-role.kubernetes.io/"+value, value)
