Feature: V2 SDK Ruby Cartridge
  @cartridge_v2_ruby
  Scenario Outline: Add cartridge, create and destroy an app
    Given a new ruby-<cart_version> type application
    Then the application git repo will exist
    And the platform-created default environment variables will exist
    And the ruby-<cart_version> cartridge private endpoints will be exposed
    And the ruby-<cart_version> RUBY_DIR env entry will exist
    And the ruby-<cart_version> RUBY_LOG_DIR env entry will exist
    And the ruby-<cart_version> RUBY_VERSION env entry will equal '<cart_version>'
    ## 'passenger-status' can't be run in the gear context
    And a <proc_name> process for <label> will be running
    When I destroy the application
    Then the application git repo will not exist

    @cartridge_v2_ruby_19
    @cartridge_extended1
    Scenarios: r1.9
      | cart_version | label     | proc_name |
      |      1.9     | Passenger | ruby      |

    @cartridge_extended1
    @cartridge_v2_ruby_18
    Scenarios: r1.8
      | cart_version | label     | proc_name |
      |      1.8     | Passenger | ruby      |
