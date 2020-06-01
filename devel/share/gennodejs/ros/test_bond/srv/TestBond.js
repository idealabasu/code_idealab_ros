// Auto-generated. Do not edit!

// (in-package test_bond.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class TestBondRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.topic = null;
      this.id = null;
      this.delay_connect = null;
      this.delay_death = null;
      this.inhibit_death = null;
      this.inhibit_death_message = null;
    }
    else {
      if (initObj.hasOwnProperty('topic')) {
        this.topic = initObj.topic
      }
      else {
        this.topic = '';
      }
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = '';
      }
      if (initObj.hasOwnProperty('delay_connect')) {
        this.delay_connect = initObj.delay_connect
      }
      else {
        this.delay_connect = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('delay_death')) {
        this.delay_death = initObj.delay_death
      }
      else {
        this.delay_death = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('inhibit_death')) {
        this.inhibit_death = initObj.inhibit_death
      }
      else {
        this.inhibit_death = false;
      }
      if (initObj.hasOwnProperty('inhibit_death_message')) {
        this.inhibit_death_message = initObj.inhibit_death_message
      }
      else {
        this.inhibit_death_message = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TestBondRequest
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    // Serialize message field [id]
    bufferOffset = _serializer.string(obj.id, buffer, bufferOffset);
    // Serialize message field [delay_connect]
    bufferOffset = _serializer.duration(obj.delay_connect, buffer, bufferOffset);
    // Serialize message field [delay_death]
    bufferOffset = _serializer.duration(obj.delay_death, buffer, bufferOffset);
    // Serialize message field [inhibit_death]
    bufferOffset = _serializer.bool(obj.inhibit_death, buffer, bufferOffset);
    // Serialize message field [inhibit_death_message]
    bufferOffset = _serializer.bool(obj.inhibit_death_message, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TestBondRequest
    let len;
    let data = new TestBondRequest(null);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [id]
    data.id = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [delay_connect]
    data.delay_connect = _deserializer.duration(buffer, bufferOffset);
    // Deserialize message field [delay_death]
    data.delay_death = _deserializer.duration(buffer, bufferOffset);
    // Deserialize message field [inhibit_death]
    data.inhibit_death = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [inhibit_death_message]
    data.inhibit_death_message = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.topic.length;
    length += object.id.length;
    return length + 26;
  }

  static datatype() {
    // Returns string type for a service object
    return 'test_bond/TestBondRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1c7d43df2e371719140975f9c404a8bb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string topic
    string id
    duration delay_connect
    duration delay_death
    bool inhibit_death
    bool inhibit_death_message
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TestBondRequest(null);
    if (msg.topic !== undefined) {
      resolved.topic = msg.topic;
    }
    else {
      resolved.topic = ''
    }

    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = ''
    }

    if (msg.delay_connect !== undefined) {
      resolved.delay_connect = msg.delay_connect;
    }
    else {
      resolved.delay_connect = {secs: 0, nsecs: 0}
    }

    if (msg.delay_death !== undefined) {
      resolved.delay_death = msg.delay_death;
    }
    else {
      resolved.delay_death = {secs: 0, nsecs: 0}
    }

    if (msg.inhibit_death !== undefined) {
      resolved.inhibit_death = msg.inhibit_death;
    }
    else {
      resolved.inhibit_death = false
    }

    if (msg.inhibit_death_message !== undefined) {
      resolved.inhibit_death_message = msg.inhibit_death_message;
    }
    else {
      resolved.inhibit_death_message = false
    }

    return resolved;
    }
};

class TestBondResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TestBondResponse
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TestBondResponse
    let len;
    let data = new TestBondResponse(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'test_bond/TestBondResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TestBondResponse(null);
    return resolved;
    }
};

module.exports = {
  Request: TestBondRequest,
  Response: TestBondResponse,
  md5sum() { return '1c7d43df2e371719140975f9c404a8bb'; },
  datatype() { return 'test_bond/TestBond'; }
};
