
(cl:in-package :asdf)

(defsystem "test_bond-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "TestBond" :depends-on ("_package_TestBond"))
    (:file "_package_TestBond" :depends-on ("_package"))
  ))