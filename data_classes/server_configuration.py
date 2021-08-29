from util.from_type import *
from data_classes.name_value_pair import NameValuePair
from data_classes.version_number import VersionNumber
from data_classes.image_saving_convention import ImageSavingConvention
from data_classes.metadata_options import MetadataOptions
from data_classes.path_substitution import PathSubstitution
from data_classes.repository_info import RepositoryInfo


@dataclass
class ServerConfiguration:
    """Represents the server configuration."""
    """Gets or sets the number of days we should retain activity logs."""
    activity_log_retention_days: Optional[int] = None
    """Gets or sets a value indicating whether Autodiscovery is enabled."""
    auto_discovery: Optional[bool] = None
    """Gets or sets a value indicating whether Autodiscovery tracing is enabled."""
    auto_discovery_tracing: Optional[bool] = None
    base_url: Optional[str] = None
    """Gets or sets the cache path."""
    cache_path: Optional[str] = None
    """Gets or sets the password required to access the X.509 certificate data in the file
    specified by MediaBrowser.Model.Configuration.ServerConfiguration.CertificatePath.
    """
    certificate_password: Optional[str] = None
    """Gets or sets the filesystem path of an X.509 certificate to use for SSL."""
    certificate_path: Optional[str] = None
    codecs_used: Optional[List[str]] = None
    content_types: Optional[List[NameValuePair]] = None
    """Gets or sets the cors hosts."""
    cors_hosts: Optional[List[str]] = None
    disable_live_tv_channel_user_data_name: Optional[bool] = None
    display_specials_within_seasons: Optional[bool] = None
    """Gets or sets a value indicating whether [enable case sensitive item ids]."""
    enable_case_sensitive_item_ids: Optional[bool] = None
    """Gets or sets a value indicating whether [enable dashboard response caching].
    Allows potential contributors without visual studio to modify production dashboard code
    and test changes.
    """
    enable_dashboard_response_caching: Optional[bool] = None
    enable_external_content_in_suggestions: Optional[bool] = None
    enable_folder_view: Optional[bool] = None
    enable_grouping_into_collections: Optional[bool] = None
    """Gets or sets a value indicating whether to use HTTPS."""
    enable_https: Optional[bool] = None
    """Gets or sets a value indicating whether IPV4 capability is enabled."""
    enable_ipv4: Optional[bool] = None
    """Gets or sets a value indicating whether IPV6 capability is enabled."""
    enable_ipv6: Optional[bool] = None
    """Gets or sets a value indicating whether to enable prometheus metrics exporting."""
    enable_metrics: Optional[bool] = None
    """Gets a value indicating whether multi-socket binding is available."""
    enable_multi_socket_binding: Optional[bool] = None
    enable_new_omdb_support: Optional[bool] = None
    enable_normalized_item_by_name_ids: Optional[bool] = None
    """Gets or sets a value indicating whether access outside of the LAN is permitted."""
    enable_remote_access: Optional[bool] = None
    """Gets or sets a value indicating whether slow server responses should be logged as a
    warning.
    """
    enable_slow_response_warning: Optional[bool] = None
    """Gets or sets a value indicating whether detailed ssdp logs are sent to the console/log.
    "Emby.Dlna": "Debug" must be set in logging.default.json for this property to work.
    """
    enable_ssdp_tracing: Optional[bool] = None
    """Gets or sets a value indicating whether to enable automatic port forwarding."""
    enable_u_pn_p: Optional[bool] = None
    """Gets or sets the time (in seconds) between the pings of SSDP gateway monitor."""
    gateway_monitor_period: Optional[int] = None
    """Gets or sets the ports that HDHomerun uses."""
    hd_homerun_port_range: Optional[str] = None
    """Gets or sets the HTTP server port number."""
    http_server_port_number: Optional[int] = None
    """Gets or sets the HTTPS server port number."""
    https_port_number: Optional[int] = None
    """Gets or sets a value indicating whether address names that match
    MediaBrowser.Model.Configuration.ServerConfiguration.VirtualInterfaceNames should be
    Ignore for the purposes of binding.
    """
    ignore_virtual_interfaces: Optional[bool] = None
    image_extraction_timeout_ms: Optional[int] = None
    """Gets or sets the image saving convention."""
    image_saving_convention: Optional[ImageSavingConvention] = None
    """Gets or sets a value indicating whether this instance is port authorized."""
    is_port_authorized: Optional[bool] = None
    """Gets or sets a value indicating whether <seealso
    cref="P:MediaBrowser.Model.Configuration.ServerConfiguration.RemoteIPFilter" /> contains
    a blacklist or a whitelist. Default is a whitelist.
    """
    is_remote_ip_filter_blacklist: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is first run."""
    is_startup_wizard_completed: Optional[bool] = None
    """Gets or sets the known proxies."""
    known_proxies: Optional[List[str]] = None
    """Gets or sets the how many metadata refreshes can run concurrently."""
    library_metadata_refresh_concurrency: Optional[int] = None
    """Gets or sets the delay in seconds that we will wait after a file system change to try and
    discover what has been added/removed
    Some delay is necessary with some items because their creation is not atomic.  It
    involves the creation of several
    different directories and files.
    """
    library_monitor_delay: Optional[int] = None
    """Gets or sets the how the library scan fans out."""
    library_scan_fanout_concurrency: Optional[int] = None
    """Gets or sets the interface addresses which Jellyfin will bind to. If empty, all
    interfaces will be used.
    """
    local_network_addresses: Optional[List[str]] = None
    """Gets or sets the subnets that are deemed to make up the LAN."""
    local_network_subnets: Optional[List[str]] = None
    """Gets or sets the number of days we should retain log files."""
    log_file_retention_days: Optional[int] = None
    """Gets or sets the remaining minutes of a book that can be played while still saving
    playstate. If this percentage is crossed playstate will be reset to the beginning and the
    item will be marked watched.
    """
    max_audiobook_resume: Optional[int] = None
    """Gets or sets the maximum percentage of an item that can be played while still saving
    playstate. If this percentage is crossed playstate will be reset to the beginning and the
    item will be marked watched.
    """
    max_resume_pct: Optional[int] = None
    """Gets or sets the metadata country code."""
    metadata_country_code: Optional[str] = None
    metadata_network_path: Optional[str] = None
    metadata_options: Optional[List[MetadataOptions]] = None
    """Gets or sets the metadata path."""
    metadata_path: Optional[str] = None
    """Gets or sets the minimum minutes of a book that must be played in order for playstate to
    be updated.
    """
    min_audiobook_resume: Optional[int] = None
    """Gets or sets the minimum duration that an item must have in order to be eligible for
    playstate updates..
    """
    min_resume_duration_seconds: Optional[int] = None
    """Gets or sets the minimum percentage of an item that must be played in order for playstate
    to be updated.
    """
    min_resume_pct: Optional[int] = None
    path_substitutions: Optional[List[PathSubstitution]] = None
    plugin_repositories: Optional[List[RepositoryInfo]] = None
    """Gets or sets the preferred metadata language."""
    preferred_metadata_language: Optional[str] = None
    """Gets or sets the last known version that was ran using the configuration."""
    previous_version: Optional[VersionNumber] = None
    """Gets or sets the stringified PreviousVersion to be stored/loaded,
    because System.Version itself isn't xml-serializable.
    """
    previous_version_str: Optional[str] = None
    """Gets or sets the public HTTPS port."""
    public_https_port: Optional[int] = None
    """Gets or sets the public mapped port."""
    public_port: Optional[int] = None
    """Gets or sets PublishedServerUri to advertise for specific subnets."""
    published_server_uri_by_subnet: Optional[List[str]] = None
    """Gets or sets a value indicating whether quick connect is available for use on this server."""
    quick_connect_available: Optional[bool] = None
    remote_client_bitrate_limit: Optional[int] = None
    """Gets or sets the filter for remote IP connectivity. Used in conjuntion with <seealso
    cref="P:MediaBrowser.Model.Configuration.ServerConfiguration.IsRemoteIPFilterBlacklist"
    />.
    """
    remote_ip_filter: Optional[List[str]] = None
    """Gets or sets a value indicating whether older plugins should automatically be deleted
    from the plugin folder.
    """
    remove_old_plugins: Optional[bool] = None
    """Gets or sets a value indicating whether the server should force connections over HTTPS."""
    require_https: Optional[bool] = None
    save_metadata_hidden: Optional[bool] = None
    server_name: Optional[str] = None
    skip_deserialization_for_basic_types: Optional[bool] = None
    """Gets or sets the threshold for the slow response time warning in ms."""
    slow_response_threshold_ms: Optional[int] = None
    """Gets or sets characters to be removed from strings to create a sort name."""
    sort_remove_characters: Optional[List[str]] = None
    """Gets or sets words to be removed from strings to create a sort name."""
    sort_remove_words: Optional[List[str]] = None
    """Gets or sets characters to be replaced with a ' ' in strings to create a sort name."""
    sort_replace_characters: Optional[List[str]] = None
    """Gets or sets a value indicating whether an IP address is to be used to filter the
    detailed ssdp logs that are being sent to the console/log.
    If the setting "Emby.Dlna": "Debug" msut be set in logging.default.json for this property
    to work.
    """
    ssdp_tracing_filter: Optional[str] = None
    """Gets or sets a value indicating whether all IPv6 interfaces should be treated as on the
    internal network.
    Depending on the address range implemented ULA ranges might not be used.
    """
    trust_all_ip6_interfaces: Optional[bool] = None
    """Gets or sets client udp port range."""
    udp_port_range: Optional[str] = None
    """Gets or sets the number of times SSDP UDP messages are sent."""
    udp_send_count: Optional[int] = None
    """Gets or sets the delay between each groups of SSDP messages (in ms)."""
    udp_send_delay: Optional[int] = None
    ui_culture: Optional[str] = None
    uninstalled_plugins: Optional[List[str]] = None
    """Gets or sets a value indicating whether the http port should be mapped as part of UPnP
    automatic port forwarding.
    """
    u_pn_p_create_http_port_map: Optional[bool] = None
    """Gets or sets a value indicating the interfaces that should be ignored. The list can be
    comma separated. <seealso
    cref="P:MediaBrowser.Model.Configuration.ServerConfiguration.IgnoreVirtualInterfaces" />.
    """
    virtual_interface_names: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ServerConfiguration':
        assert isinstance(obj, dict)
        activity_log_retention_days = from_union([from_int, from_none], obj.get("ActivityLogRetentionDays"))
        auto_discovery = from_union([from_bool, from_none], obj.get("AutoDiscovery"))
        auto_discovery_tracing = from_union([from_bool, from_none], obj.get("AutoDiscoveryTracing"))
        base_url = from_union([from_str, from_none], obj.get("BaseUrl"))
        cache_path = from_union([from_str, from_none], obj.get("CachePath"))
        certificate_password = from_union([from_str, from_none], obj.get("CertificatePassword"))
        certificate_path = from_union([from_str, from_none], obj.get("CertificatePath"))
        codecs_used = from_union([lambda x: from_list(from_str, x), from_none], obj.get("CodecsUsed"))
        content_types = from_union([lambda x: from_list(NameValuePair.from_dict, x), from_none], obj.get("ContentTypes"))
        cors_hosts = from_union([lambda x: from_list(from_str, x), from_none], obj.get("CorsHosts"))
        disable_live_tv_channel_user_data_name = from_union([from_bool, from_none], obj.get("DisableLiveTvChannelUserDataName"))
        display_specials_within_seasons = from_union([from_bool, from_none], obj.get("DisplaySpecialsWithinSeasons"))
        enable_case_sensitive_item_ids = from_union([from_bool, from_none], obj.get("EnableCaseSensitiveItemIds"))
        enable_dashboard_response_caching = from_union([from_bool, from_none], obj.get("EnableDashboardResponseCaching"))
        enable_external_content_in_suggestions = from_union([from_bool, from_none], obj.get("EnableExternalContentInSuggestions"))
        enable_folder_view = from_union([from_bool, from_none], obj.get("EnableFolderView"))
        enable_grouping_into_collections = from_union([from_bool, from_none], obj.get("EnableGroupingIntoCollections"))
        enable_https = from_union([from_bool, from_none], obj.get("EnableHttps"))
        enable_ipv4 = from_union([from_bool, from_none], obj.get("EnableIPV4"))
        enable_ipv6 = from_union([from_bool, from_none], obj.get("EnableIPV6"))
        enable_metrics = from_union([from_bool, from_none], obj.get("EnableMetrics"))
        enable_multi_socket_binding = from_union([from_bool, from_none], obj.get("EnableMultiSocketBinding"))
        enable_new_omdb_support = from_union([from_bool, from_none], obj.get("EnableNewOmdbSupport"))
        enable_normalized_item_by_name_ids = from_union([from_bool, from_none], obj.get("EnableNormalizedItemByNameIds"))
        enable_remote_access = from_union([from_bool, from_none], obj.get("EnableRemoteAccess"))
        enable_slow_response_warning = from_union([from_bool, from_none], obj.get("EnableSlowResponseWarning"))
        enable_ssdp_tracing = from_union([from_bool, from_none], obj.get("EnableSSDPTracing"))
        enable_u_pn_p = from_union([from_bool, from_none], obj.get("EnableUPnP"))
        gateway_monitor_period = from_union([from_int, from_none], obj.get("GatewayMonitorPeriod"))
        hd_homerun_port_range = from_union([from_str, from_none], obj.get("HDHomerunPortRange"))
        http_server_port_number = from_union([from_int, from_none], obj.get("HttpServerPortNumber"))
        https_port_number = from_union([from_int, from_none], obj.get("HttpsPortNumber"))
        ignore_virtual_interfaces = from_union([from_bool, from_none], obj.get("IgnoreVirtualInterfaces"))
        image_extraction_timeout_ms = from_union([from_int, from_none], obj.get("ImageExtractionTimeoutMs"))
        image_saving_convention = from_union([ImageSavingConvention, from_none], obj.get("ImageSavingConvention"))
        is_port_authorized = from_union([from_bool, from_none], obj.get("IsPortAuthorized"))
        is_remote_ip_filter_blacklist = from_union([from_bool, from_none], obj.get("IsRemoteIPFilterBlacklist"))
        is_startup_wizard_completed = from_union([from_bool, from_none], obj.get("IsStartupWizardCompleted"))
        known_proxies = from_union([lambda x: from_list(from_str, x), from_none], obj.get("KnownProxies"))
        library_metadata_refresh_concurrency = from_union([from_int, from_none], obj.get("LibraryMetadataRefreshConcurrency"))
        library_monitor_delay = from_union([from_int, from_none], obj.get("LibraryMonitorDelay"))
        library_scan_fanout_concurrency = from_union([from_int, from_none], obj.get("LibraryScanFanoutConcurrency"))
        local_network_addresses = from_union([lambda x: from_list(from_str, x), from_none], obj.get("LocalNetworkAddresses"))
        local_network_subnets = from_union([lambda x: from_list(from_str, x), from_none], obj.get("LocalNetworkSubnets"))
        log_file_retention_days = from_union([from_int, from_none], obj.get("LogFileRetentionDays"))
        max_audiobook_resume = from_union([from_int, from_none], obj.get("MaxAudiobookResume"))
        max_resume_pct = from_union([from_int, from_none], obj.get("MaxResumePct"))
        metadata_country_code = from_union([from_str, from_none], obj.get("MetadataCountryCode"))
        metadata_network_path = from_union([from_str, from_none], obj.get("MetadataNetworkPath"))
        metadata_options = from_union([lambda x: from_list(MetadataOptions.from_dict, x), from_none], obj.get("MetadataOptions"))
        metadata_path = from_union([from_str, from_none], obj.get("MetadataPath"))
        min_audiobook_resume = from_union([from_int, from_none], obj.get("MinAudiobookResume"))
        min_resume_duration_seconds = from_union([from_int, from_none], obj.get("MinResumeDurationSeconds"))
        min_resume_pct = from_union([from_int, from_none], obj.get("MinResumePct"))
        path_substitutions = from_union([lambda x: from_list(PathSubstitution.from_dict, x), from_none], obj.get("PathSubstitutions"))
        plugin_repositories = from_union([lambda x: from_list(RepositoryInfo.from_dict, x), from_none], obj.get("PluginRepositories"))
        preferred_metadata_language = from_union([from_str, from_none], obj.get("PreferredMetadataLanguage"))
        previous_version = from_union([VersionNumber.from_dict, from_none], obj.get("PreviousVersion"))
        previous_version_str = from_union([from_str, from_none], obj.get("PreviousVersionStr"))
        public_https_port = from_union([from_int, from_none], obj.get("PublicHttpsPort"))
        public_port = from_union([from_int, from_none], obj.get("PublicPort"))
        published_server_uri_by_subnet = from_union([lambda x: from_list(from_str, x), from_none], obj.get("PublishedServerUriBySubnet"))
        quick_connect_available = from_union([from_bool, from_none], obj.get("QuickConnectAvailable"))
        remote_client_bitrate_limit = from_union([from_int, from_none], obj.get("RemoteClientBitrateLimit"))
        remote_ip_filter = from_union([lambda x: from_list(from_str, x), from_none], obj.get("RemoteIPFilter"))
        remove_old_plugins = from_union([from_bool, from_none], obj.get("RemoveOldPlugins"))
        require_https = from_union([from_bool, from_none], obj.get("RequireHttps"))
        save_metadata_hidden = from_union([from_bool, from_none], obj.get("SaveMetadataHidden"))
        server_name = from_union([from_str, from_none], obj.get("ServerName"))
        skip_deserialization_for_basic_types = from_union([from_bool, from_none], obj.get("SkipDeserializationForBasicTypes"))
        slow_response_threshold_ms = from_union([from_int, from_none], obj.get("SlowResponseThresholdMs"))
        sort_remove_characters = from_union([lambda x: from_list(from_str, x), from_none], obj.get("SortRemoveCharacters"))
        sort_remove_words = from_union([lambda x: from_list(from_str, x), from_none], obj.get("SortRemoveWords"))
        sort_replace_characters = from_union([lambda x: from_list(from_str, x), from_none], obj.get("SortReplaceCharacters"))
        ssdp_tracing_filter = from_union([from_str, from_none], obj.get("SSDPTracingFilter"))
        trust_all_ip6_interfaces = from_union([from_bool, from_none], obj.get("TrustAllIP6Interfaces"))
        udp_port_range = from_union([from_str, from_none], obj.get("UDPPortRange"))
        udp_send_count = from_union([from_int, from_none], obj.get("UDPSendCount"))
        udp_send_delay = from_union([from_int, from_none], obj.get("UDPSendDelay"))
        ui_culture = from_union([from_str, from_none], obj.get("UICulture"))
        uninstalled_plugins = from_union([lambda x: from_list(from_str, x), from_none], obj.get("UninstalledPlugins"))
        u_pn_p_create_http_port_map = from_union([from_bool, from_none], obj.get("UPnPCreateHttpPortMap"))
        virtual_interface_names = from_union([from_str, from_none], obj.get("VirtualInterfaceNames"))
        return ServerConfiguration(activity_log_retention_days, auto_discovery, auto_discovery_tracing, base_url, cache_path, certificate_password, certificate_path, codecs_used, content_types, cors_hosts, disable_live_tv_channel_user_data_name, display_specials_within_seasons, enable_case_sensitive_item_ids, enable_dashboard_response_caching, enable_external_content_in_suggestions, enable_folder_view, enable_grouping_into_collections, enable_https, enable_ipv4, enable_ipv6, enable_metrics, enable_multi_socket_binding, enable_new_omdb_support, enable_normalized_item_by_name_ids, enable_remote_access, enable_slow_response_warning, enable_ssdp_tracing, enable_u_pn_p, gateway_monitor_period, hd_homerun_port_range, http_server_port_number, https_port_number, ignore_virtual_interfaces, image_extraction_timeout_ms, image_saving_convention, is_port_authorized, is_remote_ip_filter_blacklist, is_startup_wizard_completed, known_proxies, library_metadata_refresh_concurrency, library_monitor_delay, library_scan_fanout_concurrency, local_network_addresses, local_network_subnets, log_file_retention_days, max_audiobook_resume, max_resume_pct, metadata_country_code, metadata_network_path, metadata_options, metadata_path, min_audiobook_resume, min_resume_duration_seconds, min_resume_pct, path_substitutions, plugin_repositories, preferred_metadata_language, previous_version, previous_version_str, public_https_port, public_port, published_server_uri_by_subnet, quick_connect_available, remote_client_bitrate_limit, remote_ip_filter, remove_old_plugins, require_https, save_metadata_hidden, server_name, skip_deserialization_for_basic_types, slow_response_threshold_ms, sort_remove_characters, sort_remove_words, sort_replace_characters, ssdp_tracing_filter, trust_all_ip6_interfaces, udp_port_range, udp_send_count, udp_send_delay, ui_culture, uninstalled_plugins, u_pn_p_create_http_port_map, virtual_interface_names)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ActivityLogRetentionDays"] = from_union([from_int, from_none], self.activity_log_retention_days)
        result["AutoDiscovery"] = from_union([from_bool, from_none], self.auto_discovery)
        result["AutoDiscoveryTracing"] = from_union([from_bool, from_none], self.auto_discovery_tracing)
        result["BaseUrl"] = from_union([from_str, from_none], self.base_url)
        result["CachePath"] = from_union([from_str, from_none], self.cache_path)
        result["CertificatePassword"] = from_union([from_str, from_none], self.certificate_password)
        result["CertificatePath"] = from_union([from_str, from_none], self.certificate_path)
        result["CodecsUsed"] = from_union([lambda x: from_list(from_str, x), from_none], self.codecs_used)
        result["ContentTypes"] = from_union([lambda x: from_list(lambda x: to_class(NameValuePair, x), x), from_none], self.content_types)
        result["CorsHosts"] = from_union([lambda x: from_list(from_str, x), from_none], self.cors_hosts)
        result["DisableLiveTvChannelUserDataName"] = from_union([from_bool, from_none], self.disable_live_tv_channel_user_data_name)
        result["DisplaySpecialsWithinSeasons"] = from_union([from_bool, from_none], self.display_specials_within_seasons)
        result["EnableCaseSensitiveItemIds"] = from_union([from_bool, from_none], self.enable_case_sensitive_item_ids)
        result["EnableDashboardResponseCaching"] = from_union([from_bool, from_none], self.enable_dashboard_response_caching)
        result["EnableExternalContentInSuggestions"] = from_union([from_bool, from_none], self.enable_external_content_in_suggestions)
        result["EnableFolderView"] = from_union([from_bool, from_none], self.enable_folder_view)
        result["EnableGroupingIntoCollections"] = from_union([from_bool, from_none], self.enable_grouping_into_collections)
        result["EnableHttps"] = from_union([from_bool, from_none], self.enable_https)
        result["EnableIPV4"] = from_union([from_bool, from_none], self.enable_ipv4)
        result["EnableIPV6"] = from_union([from_bool, from_none], self.enable_ipv6)
        result["EnableMetrics"] = from_union([from_bool, from_none], self.enable_metrics)
        result["EnableMultiSocketBinding"] = from_union([from_bool, from_none], self.enable_multi_socket_binding)
        result["EnableNewOmdbSupport"] = from_union([from_bool, from_none], self.enable_new_omdb_support)
        result["EnableNormalizedItemByNameIds"] = from_union([from_bool, from_none], self.enable_normalized_item_by_name_ids)
        result["EnableRemoteAccess"] = from_union([from_bool, from_none], self.enable_remote_access)
        result["EnableSlowResponseWarning"] = from_union([from_bool, from_none], self.enable_slow_response_warning)
        result["EnableSSDPTracing"] = from_union([from_bool, from_none], self.enable_ssdp_tracing)
        result["EnableUPnP"] = from_union([from_bool, from_none], self.enable_u_pn_p)
        result["GatewayMonitorPeriod"] = from_union([from_int, from_none], self.gateway_monitor_period)
        result["HDHomerunPortRange"] = from_union([from_str, from_none], self.hd_homerun_port_range)
        result["HttpServerPortNumber"] = from_union([from_int, from_none], self.http_server_port_number)
        result["HttpsPortNumber"] = from_union([from_int, from_none], self.https_port_number)
        result["IgnoreVirtualInterfaces"] = from_union([from_bool, from_none], self.ignore_virtual_interfaces)
        result["ImageExtractionTimeoutMs"] = from_union([from_int, from_none], self.image_extraction_timeout_ms)
        result["ImageSavingConvention"] = from_union([lambda x: to_enum(ImageSavingConvention, x), from_none], self.image_saving_convention)
        result["IsPortAuthorized"] = from_union([from_bool, from_none], self.is_port_authorized)
        result["IsRemoteIPFilterBlacklist"] = from_union([from_bool, from_none], self.is_remote_ip_filter_blacklist)
        result["IsStartupWizardCompleted"] = from_union([from_bool, from_none], self.is_startup_wizard_completed)
        result["KnownProxies"] = from_union([lambda x: from_list(from_str, x), from_none], self.known_proxies)
        result["LibraryMetadataRefreshConcurrency"] = from_union([from_int, from_none], self.library_metadata_refresh_concurrency)
        result["LibraryMonitorDelay"] = from_union([from_int, from_none], self.library_monitor_delay)
        result["LibraryScanFanoutConcurrency"] = from_union([from_int, from_none], self.library_scan_fanout_concurrency)
        result["LocalNetworkAddresses"] = from_union([lambda x: from_list(from_str, x), from_none], self.local_network_addresses)
        result["LocalNetworkSubnets"] = from_union([lambda x: from_list(from_str, x), from_none], self.local_network_subnets)
        result["LogFileRetentionDays"] = from_union([from_int, from_none], self.log_file_retention_days)
        result["MaxAudiobookResume"] = from_union([from_int, from_none], self.max_audiobook_resume)
        result["MaxResumePct"] = from_union([from_int, from_none], self.max_resume_pct)
        result["MetadataCountryCode"] = from_union([from_str, from_none], self.metadata_country_code)
        result["MetadataNetworkPath"] = from_union([from_str, from_none], self.metadata_network_path)
        result["MetadataOptions"] = from_union([lambda x: from_list(lambda x: to_class(MetadataOptions, x), x), from_none], self.metadata_options)
        result["MetadataPath"] = from_union([from_str, from_none], self.metadata_path)
        result["MinAudiobookResume"] = from_union([from_int, from_none], self.min_audiobook_resume)
        result["MinResumeDurationSeconds"] = from_union([from_int, from_none], self.min_resume_duration_seconds)
        result["MinResumePct"] = from_union([from_int, from_none], self.min_resume_pct)
        result["PathSubstitutions"] = from_union([lambda x: from_list(lambda x: to_class(PathSubstitution, x), x), from_none], self.path_substitutions)
        result["PluginRepositories"] = from_union([lambda x: from_list(lambda x: to_class(RepositoryInfo, x), x), from_none], self.plugin_repositories)
        result["PreferredMetadataLanguage"] = from_union([from_str, from_none], self.preferred_metadata_language)
        result["PreviousVersion"] = from_union([lambda x: to_class(VersionNumber, x), from_none], self.previous_version)
        result["PreviousVersionStr"] = from_union([from_str, from_none], self.previous_version_str)
        result["PublicHttpsPort"] = from_union([from_int, from_none], self.public_https_port)
        result["PublicPort"] = from_union([from_int, from_none], self.public_port)
        result["PublishedServerUriBySubnet"] = from_union([lambda x: from_list(from_str, x), from_none], self.published_server_uri_by_subnet)
        result["QuickConnectAvailable"] = from_union([from_bool, from_none], self.quick_connect_available)
        result["RemoteClientBitrateLimit"] = from_union([from_int, from_none], self.remote_client_bitrate_limit)
        result["RemoteIPFilter"] = from_union([lambda x: from_list(from_str, x), from_none], self.remote_ip_filter)
        result["RemoveOldPlugins"] = from_union([from_bool, from_none], self.remove_old_plugins)
        result["RequireHttps"] = from_union([from_bool, from_none], self.require_https)
        result["SaveMetadataHidden"] = from_union([from_bool, from_none], self.save_metadata_hidden)
        result["ServerName"] = from_union([from_str, from_none], self.server_name)
        result["SkipDeserializationForBasicTypes"] = from_union([from_bool, from_none], self.skip_deserialization_for_basic_types)
        result["SlowResponseThresholdMs"] = from_union([from_int, from_none], self.slow_response_threshold_ms)
        result["SortRemoveCharacters"] = from_union([lambda x: from_list(from_str, x), from_none], self.sort_remove_characters)
        result["SortRemoveWords"] = from_union([lambda x: from_list(from_str, x), from_none], self.sort_remove_words)
        result["SortReplaceCharacters"] = from_union([lambda x: from_list(from_str, x), from_none], self.sort_replace_characters)
        result["SSDPTracingFilter"] = from_union([from_str, from_none], self.ssdp_tracing_filter)
        result["TrustAllIP6Interfaces"] = from_union([from_bool, from_none], self.trust_all_ip6_interfaces)
        result["UDPPortRange"] = from_union([from_str, from_none], self.udp_port_range)
        result["UDPSendCount"] = from_union([from_int, from_none], self.udp_send_count)
        result["UDPSendDelay"] = from_union([from_int, from_none], self.udp_send_delay)
        result["UICulture"] = from_union([from_str, from_none], self.ui_culture)
        result["UninstalledPlugins"] = from_union([lambda x: from_list(from_str, x), from_none], self.uninstalled_plugins)
        result["UPnPCreateHttpPortMap"] = from_union([from_bool, from_none], self.u_pn_p_create_http_port_map)
        result["VirtualInterfaceNames"] = from_union([from_str, from_none], self.virtual_interface_names)
        return result


