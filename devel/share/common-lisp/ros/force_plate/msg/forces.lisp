; Auto-generated. Do not edit!


(cl:in-package force_plate-msg)


;//! \htmlinclude forces.msg.html

(cl:defclass <forces> (roslisp-msg-protocol:ros-message)
  ((f1
    :reader f1
    :initarg :f1
    :type cl:float
    :initform 0.0)
   (f2
    :reader f2
    :initarg :f2
    :type cl:float
    :initform 0.0)
   (f3
    :reader f3
    :initarg :f3
    :type cl:float
    :initform 0.0)
   (f4
    :reader f4
    :initarg :f4
    :type cl:float
    :initform 0.0))
)

(cl:defclass forces (<forces>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <forces>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'forces)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name force_plate-msg:<forces> is deprecated: use force_plate-msg:forces instead.")))

(cl:ensure-generic-function 'f1-val :lambda-list '(m))
(cl:defmethod f1-val ((m <forces>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader force_plate-msg:f1-val is deprecated.  Use force_plate-msg:f1 instead.")
  (f1 m))

(cl:ensure-generic-function 'f2-val :lambda-list '(m))
(cl:defmethod f2-val ((m <forces>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader force_plate-msg:f2-val is deprecated.  Use force_plate-msg:f2 instead.")
  (f2 m))

(cl:ensure-generic-function 'f3-val :lambda-list '(m))
(cl:defmethod f3-val ((m <forces>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader force_plate-msg:f3-val is deprecated.  Use force_plate-msg:f3 instead.")
  (f3 m))

(cl:ensure-generic-function 'f4-val :lambda-list '(m))
(cl:defmethod f4-val ((m <forces>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader force_plate-msg:f4-val is deprecated.  Use force_plate-msg:f4 instead.")
  (f4 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <forces>) ostream)
  "Serializes a message object of type '<forces>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'f1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'f2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'f3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'f4))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <forces>) istream)
  "Deserializes a message object of type '<forces>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'f1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'f2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'f3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'f4) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<forces>)))
  "Returns string type for a message object of type '<forces>"
  "force_plate/forces")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'forces)))
  "Returns string type for a message object of type 'forces"
  "force_plate/forces")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<forces>)))
  "Returns md5sum for a message object of type '<forces>"
  "5c28bd9029eb1eda370389d9a92395b2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'forces)))
  "Returns md5sum for a message object of type 'forces"
  "5c28bd9029eb1eda370389d9a92395b2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<forces>)))
  "Returns full string definition for message of type '<forces>"
  (cl:format cl:nil "float32 f1~%float32 f2~%float32 f3~%float32 f4~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'forces)))
  "Returns full string definition for message of type 'forces"
  (cl:format cl:nil "float32 f1~%float32 f2~%float32 f3~%float32 f4~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <forces>))
  (cl:+ 0
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <forces>))
  "Converts a ROS message object to a list"
  (cl:list 'forces
    (cl:cons ':f1 (f1 msg))
    (cl:cons ':f2 (f2 msg))
    (cl:cons ':f3 (f3 msg))
    (cl:cons ':f4 (f4 msg))
))
