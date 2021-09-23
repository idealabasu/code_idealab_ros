// Auto-generated. Do not edit!

// (in-package universal_robots.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class position_command {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.p = null;
    }
    else {
      if (initObj.hasOwnProperty('p')) {
        this.p = initObj.p
      }
      else {
        this.p = new Array(3).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type position_command
    // Check that the constant length array field [p] has the right length
    if (obj.p.length !== 3) {
      throw new Error('Unable to serialize array field p - length must be 3')
    }
    // Serialize message field [p]
    bufferOffset = _arraySerializer.float64(obj.p, buffer, bufferOffset, 3);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type position_command
    let len;
    let data = new position_command(null);
    // Deserialize message field [p]
    data.p = _arrayDeserializer.float64(buffer, bufferOffset, 3)
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'universal_robots/position_command';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1abbaca176899a0863a2922ff57df9ac';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[3] p
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new position_command(null);
    if (msg.p !== undefined) {
      resolved.p = msg.p;
    }
    else {
      resolved.p = new Array(3).fill(0)
    }

    return resolved;
    }
};

module.exports = position_command;
