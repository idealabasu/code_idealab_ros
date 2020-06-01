;; Auto-generated. Do not edit!


(when (boundp 'test_bond::TestBond)
  (if (not (find-package "TEST_BOND"))
    (make-package "TEST_BOND"))
  (shadow 'TestBond (find-package "TEST_BOND")))
(unless (find-package "TEST_BOND::TESTBOND")
  (make-package "TEST_BOND::TESTBOND"))
(unless (find-package "TEST_BOND::TESTBONDREQUEST")
  (make-package "TEST_BOND::TESTBONDREQUEST"))
(unless (find-package "TEST_BOND::TESTBONDRESPONSE")
  (make-package "TEST_BOND::TESTBONDRESPONSE"))

(in-package "ROS")





(defclass test_bond::TestBondRequest
  :super ros::object
  :slots (_topic _id _delay_connect _delay_death _inhibit_death _inhibit_death_message ))

(defmethod test_bond::TestBondRequest
  (:init
   (&key
    ((:topic __topic) "")
    ((:id __id) "")
    ((:delay_connect __delay_connect) (instance ros::time :init))
    ((:delay_death __delay_death) (instance ros::time :init))
    ((:inhibit_death __inhibit_death) nil)
    ((:inhibit_death_message __inhibit_death_message) nil)
    )
   (send-super :init)
   (setq _topic (string __topic))
   (setq _id (string __id))
   (setq _delay_connect __delay_connect)
   (setq _delay_death __delay_death)
   (setq _inhibit_death __inhibit_death)
   (setq _inhibit_death_message __inhibit_death_message)
   self)
  (:topic
   (&optional __topic)
   (if __topic (setq _topic __topic)) _topic)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:delay_connect
   (&optional __delay_connect)
   (if __delay_connect (setq _delay_connect __delay_connect)) _delay_connect)
  (:delay_death
   (&optional __delay_death)
   (if __delay_death (setq _delay_death __delay_death)) _delay_death)
  (:inhibit_death
   (&optional __inhibit_death)
   (if __inhibit_death (setq _inhibit_death __inhibit_death)) _inhibit_death)
  (:inhibit_death_message
   (&optional __inhibit_death_message)
   (if __inhibit_death_message (setq _inhibit_death_message __inhibit_death_message)) _inhibit_death_message)
  (:serialization-length
   ()
   (+
    ;; string _topic
    4 (length _topic)
    ;; string _id
    4 (length _id)
    ;; duration _delay_connect
    8
    ;; duration _delay_death
    8
    ;; bool _inhibit_death
    1
    ;; bool _inhibit_death_message
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _topic
       (write-long (length _topic) s) (princ _topic s)
     ;; string _id
       (write-long (length _id) s) (princ _id s)
     ;; duration _delay_connect
       (write-long (send _delay_connect :sec) s) (write-long (send _delay_connect :nsec) s)
     ;; duration _delay_death
       (write-long (send _delay_death :sec) s) (write-long (send _delay_death :nsec) s)
     ;; bool _inhibit_death
       (if _inhibit_death (write-byte -1 s) (write-byte 0 s))
     ;; bool _inhibit_death_message
       (if _inhibit_death_message (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _topic
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _topic (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; duration _delay_connect
     (send _delay_connect :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _delay_connect :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; duration _delay_death
     (send _delay_death :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _delay_death :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool _inhibit_death
     (setq _inhibit_death (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _inhibit_death_message
     (setq _inhibit_death_message (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass test_bond::TestBondResponse
  :super ros::object
  :slots ())

(defmethod test_bond::TestBondResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass test_bond::TestBond
  :super ros::object
  :slots ())

(setf (get test_bond::TestBond :md5sum-) "1c7d43df2e371719140975f9c404a8bb")
(setf (get test_bond::TestBond :datatype-) "test_bond/TestBond")
(setf (get test_bond::TestBond :request) test_bond::TestBondRequest)
(setf (get test_bond::TestBond :response) test_bond::TestBondResponse)

(defmethod test_bond::TestBondRequest
  (:response () (instance test_bond::TestBondResponse :init)))

(setf (get test_bond::TestBondRequest :md5sum-) "1c7d43df2e371719140975f9c404a8bb")
(setf (get test_bond::TestBondRequest :datatype-) "test_bond/TestBondRequest")
(setf (get test_bond::TestBondRequest :definition-)
      "string topic
string id
duration delay_connect
duration delay_death
bool inhibit_death
bool inhibit_death_message
---

")

(setf (get test_bond::TestBondResponse :md5sum-) "1c7d43df2e371719140975f9c404a8bb")
(setf (get test_bond::TestBondResponse :datatype-) "test_bond/TestBondResponse")
(setf (get test_bond::TestBondResponse :definition-)
      "string topic
string id
duration delay_connect
duration delay_death
bool inhibit_death
bool inhibit_death_message
---

")



(provide :test_bond/TestBond "1c7d43df2e371719140975f9c404a8bb")


