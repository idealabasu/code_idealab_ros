; Auto-generated. Do not edit!


(cl:in-package test_bond-srv)


;//! \htmlinclude TestBond-request.msg.html

(cl:defclass <TestBond-request> (roslisp-msg-protocol:ros-message)
  ((topic
    :reader topic
    :initarg :topic
    :type cl:string
    :initform "")
   (id
    :reader id
    :initarg :id
    :type cl:string
    :initform "")
   (delay_connect
    :reader delay_connect
    :initarg :delay_connect
    :type cl:real
    :initform 0)
   (delay_death
    :reader delay_death
    :initarg :delay_death
    :type cl:real
    :initform 0)
   (inhibit_death
    :reader inhibit_death
    :initarg :inhibit_death
    :type cl:boolean
    :initform cl:nil)
   (inhibit_death_message
    :reader inhibit_death_message
    :initarg :inhibit_death_message
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass TestBond-request (<TestBond-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TestBond-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TestBond-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test_bond-srv:<TestBond-request> is deprecated: use test_bond-srv:TestBond-request instead.")))

(cl:ensure-generic-function 'topic-val :lambda-list '(m))
(cl:defmethod topic-val ((m <TestBond-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_bond-srv:topic-val is deprecated.  Use test_bond-srv:topic instead.")
  (topic m))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <TestBond-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_bond-srv:id-val is deprecated.  Use test_bond-srv:id instead.")
  (id m))

(cl:ensure-generic-function 'delay_connect-val :lambda-list '(m))
(cl:defmethod delay_connect-val ((m <TestBond-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_bond-srv:delay_connect-val is deprecated.  Use test_bond-srv:delay_connect instead.")
  (delay_connect m))

(cl:ensure-generic-function 'delay_death-val :lambda-list '(m))
(cl:defmethod delay_death-val ((m <TestBond-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_bond-srv:delay_death-val is deprecated.  Use test_bond-srv:delay_death instead.")
  (delay_death m))

(cl:ensure-generic-function 'inhibit_death-val :lambda-list '(m))
(cl:defmethod inhibit_death-val ((m <TestBond-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_bond-srv:inhibit_death-val is deprecated.  Use test_bond-srv:inhibit_death instead.")
  (inhibit_death m))

(cl:ensure-generic-function 'inhibit_death_message-val :lambda-list '(m))
(cl:defmethod inhibit_death_message-val ((m <TestBond-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_bond-srv:inhibit_death_message-val is deprecated.  Use test_bond-srv:inhibit_death_message instead.")
  (inhibit_death_message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TestBond-request>) ostream)
  "Serializes a message object of type '<TestBond-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'topic))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'topic))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'id))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'delay_connect)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'delay_connect) (cl:floor (cl:slot-value msg 'delay_connect)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'delay_death)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'delay_death) (cl:floor (cl:slot-value msg 'delay_death)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'inhibit_death) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'inhibit_death_message) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TestBond-request>) istream)
  "Deserializes a message object of type '<TestBond-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'topic) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'topic) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'delay_connect) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'delay_death) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:setf (cl:slot-value msg 'inhibit_death) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'inhibit_death_message) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TestBond-request>)))
  "Returns string type for a service object of type '<TestBond-request>"
  "test_bond/TestBondRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TestBond-request)))
  "Returns string type for a service object of type 'TestBond-request"
  "test_bond/TestBondRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TestBond-request>)))
  "Returns md5sum for a message object of type '<TestBond-request>"
  "1c7d43df2e371719140975f9c404a8bb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TestBond-request)))
  "Returns md5sum for a message object of type 'TestBond-request"
  "1c7d43df2e371719140975f9c404a8bb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TestBond-request>)))
  "Returns full string definition for message of type '<TestBond-request>"
  (cl:format cl:nil "string topic~%string id~%duration delay_connect~%duration delay_death~%bool inhibit_death~%bool inhibit_death_message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TestBond-request)))
  "Returns full string definition for message of type 'TestBond-request"
  (cl:format cl:nil "string topic~%string id~%duration delay_connect~%duration delay_death~%bool inhibit_death~%bool inhibit_death_message~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TestBond-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'topic))
     4 (cl:length (cl:slot-value msg 'id))
     8
     8
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TestBond-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TestBond-request
    (cl:cons ':topic (topic msg))
    (cl:cons ':id (id msg))
    (cl:cons ':delay_connect (delay_connect msg))
    (cl:cons ':delay_death (delay_death msg))
    (cl:cons ':inhibit_death (inhibit_death msg))
    (cl:cons ':inhibit_death_message (inhibit_death_message msg))
))
;//! \htmlinclude TestBond-response.msg.html

(cl:defclass <TestBond-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass TestBond-response (<TestBond-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TestBond-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TestBond-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test_bond-srv:<TestBond-response> is deprecated: use test_bond-srv:TestBond-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TestBond-response>) ostream)
  "Serializes a message object of type '<TestBond-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TestBond-response>) istream)
  "Deserializes a message object of type '<TestBond-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TestBond-response>)))
  "Returns string type for a service object of type '<TestBond-response>"
  "test_bond/TestBondResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TestBond-response)))
  "Returns string type for a service object of type 'TestBond-response"
  "test_bond/TestBondResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TestBond-response>)))
  "Returns md5sum for a message object of type '<TestBond-response>"
  "1c7d43df2e371719140975f9c404a8bb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TestBond-response)))
  "Returns md5sum for a message object of type 'TestBond-response"
  "1c7d43df2e371719140975f9c404a8bb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TestBond-response>)))
  "Returns full string definition for message of type '<TestBond-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TestBond-response)))
  "Returns full string definition for message of type 'TestBond-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TestBond-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TestBond-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TestBond-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TestBond)))
  'TestBond-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TestBond)))
  'TestBond-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TestBond)))
  "Returns string type for a service object of type '<TestBond>"
  "test_bond/TestBond")