// Auto-generated. Do not edit!

// (in-package force_plate.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class forces {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.f1 = null;
      this.f2 = null;
      this.f3 = null;
      this.f4 = null;
    }
    else {
      if (initObj.hasOwnProperty('f1')) {
        this.f1 = initObj.f1
      }
      else {
        this.f1 = 0.0;
      }
      if (initObj.hasOwnProperty('f2')) {
        this.f2 = initObj.f2
      }
      else {
        this.f2 = 0.0;
      }
      if (initObj.hasOwnProperty('f3')) {
        this.f3 = initObj.f3
      }
      else {
        this.f3 = 0.0;
      }
      if (initObj.hasOwnProperty('f4')) {
        this.f4 = initObj.f4
      }
      else {
        this.f4 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type forces
    // Serialize message field [f1]
    bufferOffset = _serializer.float32(obj.f1, buffer, bufferOffset);
    // Serialize message field [f2]
    bufferOffset = _serializer.float32(obj.f2, buffer, bufferOffset);
    // Serialize message field [f3]
    bufferOffset = _serializer.float32(obj.f3, buffer, bufferOffset);
    // Serialize message field [f4]
    bufferOffset = _serializer.float32(obj.f4, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type forces
    let len;
    let data = new forces(null);
    // Deserialize message field [f1]
    data.f1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [f2]
    data.f2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [f3]
    data.f3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [f4]
    data.f4 = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'force_plate/forces';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5c28bd9029eb1eda370389d9a92395b2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 f1
    float32 f2
    float32 f3
    float32 f4
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new forces(null);
    if (msg.f1 !== undefined) {
      resolved.f1 = msg.f1;
    }
    else {
      resolved.f1 = 0.0
    }

    if (msg.f2 !== undefined) {
      resolved.f2 = msg.f2;
    }
    else {
      resolved.f2 = 0.0
    }

    if (msg.f3 !== undefined) {
      resolved.f3 = msg.f3;
    }
    else {
      resolved.f3 = 0.0
    }

    if (msg.f4 !== undefined) {
      resolved.f4 = msg.f4;
    }
    else {
      resolved.f4 = 0.0
    }

    return resolved;
    }
};

module.exports = forces;
