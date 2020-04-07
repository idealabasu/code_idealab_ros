// Auto-generated. Do not edit!

// (in-package thorlabs_linear_actuator.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class write {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.register = null;
      this.value = null;
    }
    else {
      if (initObj.hasOwnProperty('register')) {
        this.register = initObj.register
      }
      else {
        this.register = 0;
      }
      if (initObj.hasOwnProperty('value')) {
        this.value = initObj.value
      }
      else {
        this.value = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type write
    // Serialize message field [register]
    bufferOffset = _serializer.uint8(obj.register, buffer, bufferOffset);
    // Serialize message field [value]
    bufferOffset = _serializer.uint8(obj.value, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type write
    let len;
    let data = new write(null);
    // Deserialize message field [register]
    data.register = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [value]
    data.value = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 2;
  }

  static datatype() {
    // Returns string type for a message object
    return 'thorlabs_linear_actuator/write';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '42a1ebb3a1d2bdfda4b28ad577afa942';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 register
    uint8 value
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new write(null);
    if (msg.register !== undefined) {
      resolved.register = msg.register;
    }
    else {
      resolved.register = 0
    }

    if (msg.value !== undefined) {
      resolved.value = msg.value;
    }
    else {
      resolved.value = 0
    }

    return resolved;
    }
};

module.exports = write;
