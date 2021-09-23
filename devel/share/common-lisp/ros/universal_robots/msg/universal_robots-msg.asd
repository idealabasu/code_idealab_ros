
(cl:in-package :asdf)

(defsystem "universal_robots-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "position" :depends-on ("_package_position"))
    (:file "_package_position" :depends-on ("_package"))
    (:file "position_command" :depends-on ("_package_position_command"))
    (:file "_package_position_command" :depends-on ("_package"))
  ))